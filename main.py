import requests


def send_message():
    url_request = "https://discord.com/api/webhooks/829138873367265332/UO7E2arty7yyugkfHoAI_uCzB9PQowh7Nc1F9Kc6DaMm0jjwf4ebBNU34Bxq4dpsNAKw"

    headers = {"Content-Type": "application/json"}

    params = {
        "username": "joaopuccini-bot",
        "avatar_url": "https://media-exp1.licdn.com/dms/image/C4D03AQGDqjr8uiFyiA/profile-displayphoto-shrink_800_800/0/1611165583603?e=1623283200&v=beta&t=9G8p_k4WSN97Jiqu3gElPsOxfUkhLnR6co4uqk4lMos",
        "content": "**Diretamente de um python :rocket: :rocket: :rocket: :rocket: :rocket:**",
        "embeds": [
        {
            "author": {
                "name": "Linkedin => João Pedro Porto Puccini",
                "url": "https://www.linkedin.com/in/joaopuccini/",
            },
            "title": "Linkedin",
            "url": "https://www.linkedin.com/in/joaopuccini/",
            "description": "Estudante de computação no Instituto Federal de Tecnologia (IF), ávido em enfrentar"
                           " desafios e solucionar problemas, apaixonado por aprender novas tecnologias."
                           " Além de estar engajado com projetos extracurriculares como iniciação científica e"
                           " projetos finais da faculdade. Atualmente trabalhando no mundo financeiro."
                           " Possuo familiaridade com **C++**, **Java**, **Python**, **C#**"
                           ", **Web (HTML,CSS)** e no momento mais"
                           " sobre **NodeJS**, **Python**, **Java**, **Lambda** e **Containers**."
                           " Atualmente experiência mais sólida "
                           "com as tecnologias **Node**, **Python**, **Containers(Docker e Podman)**, **microserviços**"
                           ", **SQL** e **NoSQL**. ",
            # "description": "Text message. You can use Markdown here. *Italic* **bold** __underline__ ~~strikeout~~ [hyperlink](https://google.com) `code`",
            "color": 8454143,
        }
    ]
    }

    cont = 1
    while cont <= 2:
        print("Sending message to discord channel.")
        requests.post(url_request, json=params, headers=headers)
        print("Message sent to discord channel {}".format(str(cont)))
        cont = cont + 1


if __name__ == '__main__':
    send_message()

