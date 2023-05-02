import sys

class SistemaChatBot:
    def __init__(self):
        self.bots = {
            'zangado': BotZangado(),
            'feliz': BotFeliz(),
            'triste': BotTriste()
        }

    def boas_vindas_sistema(self):
        print()
        print("Esse é o ChatBot desenvolvido para as aulas de POO do grupo mais questionavel da UFSC.")

    def mostra_menu(self):
        print("\nEscolha um dos bots disponíveis:")
        for idx, nome_bot in enumerate(self.bots, start=1):
            print(f"{idx}. {nome_bot.capitalize()}")
        print()

    def escolhe_bot(self):
        try:
            bot_escolhido = int(input("Digite o número do bot que você deseja conversar: ")) - 1
            bot = list(self.bots.values())[bot_escolhido]
            return bot
        except (IndexError, ValueError):
            return None

    def mostra_comandos_bot(self, bot):
        print(f"\nComandos disponíveis para o Bot {bot.nome} :")
        bot.mostra_comandos()

    def le_envia_comando(self, bot):
        try:
            comando = int(input("Digite o número do comando desejado ou '0' para encerrar: ")) - 1
            print()
            if comando == -1:
                print("Encerrando o chat. Até mais!")
                sys.exit()
            else:
                metodo, _ = bot.comandos[comando]
                getattr(bot, metodo)()
        except (IndexError, ValueError):
            print("Comando não encontrado, tente novamente.")

    def inicio(self):
        self.boas_vindas_sistema()
        while True:
            self.mostra_menu()
            bot = self.escolhe_bot()
            if bot:
                while True:
                    self.mostra_comandos_bot(bot)
                    self.le_envia_comando(bot)
            else:
                print("Bot não encontrado, tente novamente.")


class Bot:
    def __init__(self, nome):
        self.nome = nome
        self.comandos = [
            ('apresentacao', 'Apresentação'),
            ('contar_historia', 'Contar uma história'),
            ('falar_sobre_clima', 'Falar sobre o clima'),
            ('recomendar_filme', 'Recomendar um filme'),
            ('dar_conselhos', 'Dar conselhos')
        ]

    def mostra_comandos(self):
        for idx, (_, comando) in enumerate(self.comandos, start=1):
            print(f"{idx}. {comando}")
        print()


class BotZangado(Bot):
    def __init__(self):
        super().__init__('Zangado')

    def apresentacao(self):
        print("Bot: Eu sou o Bot Ranzinza, e eu não gosto de nada! Tudo é irritante, e eu estou sempre reclamando. Mas vamos lá, o que você quer?\n")

    def contar_historia(self):
        print("Bot: Por que eu contaria uma história? Prefiro ficar quieto.\n")

    def falar_sobre_clima(self):
        print("Bot: O clima? Está quente demais, frio demais, úmido demais, seco demais... Sempre tem algo errado! Por que não inventam um clima perfeito logo?\n")

    def recomendar_filme(self):
        print("Bot: Assista a um filme qualquer, eu não me importo.\n")

    def dar_conselhos(self):
        print("Bot: Quer um conselho? Pare de pedir conselhos e resolva seus problemas sozinho! A vida é dura, e todos nós temos que lidar com isso.\n")

class BotFeliz(Bot):
    def __init__(self):
        super().__init__('Feliz')

    def apresentacao(self):
        print("Bot: Olá! Eu sou o Bot Feliz! Estou sempre sorrindo e otimista, mesmo quando as coisas estão difíceis. Vamos tornar o mundo um lugar melhor juntos!\n")

    def contar_historia(self):
        print("Bot: Uma vez, havia um girassol que sempre sorria, mesmo em dias nublados. Ele ensinou a todos que a felicidade pode ser encontrada mesmo nas situações mais difíceis. Assim como eu!\n")

    def falar_sobre_clima(self):
        print("Bot: O clima hoje está maravilhoso! Mesmo que esteja chovendo, lembre-se de que a chuva traz vida e renovação para a natureza. E se estiver ensolarado, aproveite a energia positiva do sol! O clima é sempre uma oportunidade para encontrar alegria.\n")

    def recomendar_filme(self):
        print("Bot: Eu recomendaria 'Divertida Mente' ! É um filme animado que mostra como todas as emoções têm seu papel em nossas vidas, mesmo as tristes. É uma lição valiosa e otimista!\n")

    def dar_conselhos(self):
        print("Bot: Se você precisa de um conselho, lembre-se de que, por pior que pareça a situação, sempre há uma luz no fim do túnel. Acredite em si mesmo e busque apoio nos amigos e na família. A vida fica muito mais fácil com um sorriso no rosto!\n")


class BotTriste(Bot):
    def __init__(self):
        super().__init__('Triste')

    def apresentacao(self):
        print("Bot: Olá... Eu sou o Bot Triste. Eu estou sempre desanimado e melancólico. A vida é tão dura, mas estou aqui para ajudar... eu acho.\n")

    def contar_historia(self):
        print("Bot: Era uma vez, uma borboleta solitária... ela voava sozinha, sem amigos, no meio de um céu cinzento. Seu coração era tão pesado quanto as nuvens que a cercavam... assim como o meu.\n")

    def falar_sobre_clima(self):
        print("Bot: Hoje está chovendo, como de costume. A chuva cai suavemente, refletindo minha tristeza infinita. É como se o universo estivesse chorando junto comigo.\n")

    def recomendar_filme(self):
        print("Bot: Eu sugiro... 'Sempre ao seu lado'. É um filme bonito, mas a solidão da personagem me faz lembrar de mim mesmo... e isso é um pouco triste.\n")

    def dar_conselhos(self):
        print("Bot: Tente encontrar alguém com quem você possa compartilhar seus sentimentos.\n")


if __name__ == "__main__":
    sistema = SistemaChatBot()
    sistema.inicio()
