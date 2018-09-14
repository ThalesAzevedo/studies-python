from requests import get
from bs4 import BeautifulSoup as soup


def getPage(url):           # Retirar o código fonte
    page_html = get(url, timeout=3)
    page = soup(page_html.content, 'lxml')
    return page


def getLinks(page):         # Encontra todos os links do site
    links = set()
    for a in page.find_all('a', href=True):
        if a.get('href')[:15] == url[:15]:
            links.add(a.get('href'))
    return links

def getRecipe(page):        # Encontra todos os itens da receita
    if 'Receita de' in page.find('h1').text:
        recipe = []
    # Encontra o título da receita
        title = page.find('h1').text
        recipe.append(title[11:])
    # Encontra o tipo de Receita
        tipo = page.find('span', class_='property para').get_text()
        recipe.append(tipo)
    # Encontra a duração da Receita
        tempo = page.find('span', class_='property duracion').get_text()
        recipe.append(tempo)
    # Encontra a quantidade de porções da Receita
        porcao = page.find('span', class_='property comensales').get_text()
        recipe.append(porcao)
    # Encontra a dificuldade da Receita
        dificuldade = page.find('span', class_='property dificultad').get_text()
        recipe.append(dificuldade)
    # Encontra a lista de ingredientes
        ingredientes = []
        li_list = page.find_all('li', class_='ingrediente')
        for li in li_list:
            ingrediente = li.text.replace('\n', '')
            ingredientes.append(ingrediente)
        recipe.append(ingredientes)
    # Encontra a lista de etapas da Receita
        preparo = []
        div_list = page.find_all('div', class_='apartado')
        for div in div_list:
            text = div.p.get_text()
            preparo.append(text)
        recipe.append(preparo)

        for i in recipe:
            print(i) 
        return recipe
    else:
        print('Não tem receita.')
        return

def crawl(start_url):           # Navega pelo site retirando receitas
    seen_links = set([start_url])
    available_links = set([start_url])

    while available_links:
        first_link = available_links.pop()
        page = getPage(first_link)
        seen_links.add(first_link)
        for link in getLinks(page):
            if link not in seen_links:
                available_links.add(link)
        print(len(available_links))
        print(first_link)
        print(getRecipe(page))

    return

urls = ['https://www.tudoreceitas.com/receita-de-bolo-de-chocolate-vulcao-6300.html','https://www.tudoreceitas.com/']
url = urls[1]


crawl(url)