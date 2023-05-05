class SistemaChatBot:
    def __init__(self, lista_bots):
        self.__lista_bots = lista_bots
        self.__bot: Bot = None

    def escolhe_bot(self):
        print("Escolha um Bot:")
        for i, bot in enumerate(self.__lista_bots):
            print(f"{i + 1}: {bot.nome()}")
        bot_num = int(input())
        self.__bot = self.__lista_bots[bot_num - 1]
        self.mostra_comandos_bot()

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()

    def le_envia_comando(self, comando):
        self.__bot.executa_comando(comando)

    def inicio(self):
        self.escolhe_bot()
        comando = int(input("Coloque aqui o comando\n"))
        while comando != -1:
            self.mostra_comandos_bot()
            self.le_envia_comando(comando)
            if comando == 3: self.escolhe_bot()
            comando = int(input("Coloque aqui o comando"))


class Comando:
    def __init__(self, id, mensagem, respostas=[]):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    def id(self):
        return self.__id

    def mensagem(self):
        return self.__mensagem

    def getRandomResposta(self):
        pass

    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    def delResposta(self, resposta):
        self.__respostas.remove(resposta)


class Cumprimento:
    def __init__(self, boas_vindas, apresentacao, despedida):
        self.__boas_vindas = boas_vindas
        self.__apresentacao = apresentacao
        self.__despedida = despedida

    def boas_vindas(self):
        return self.__boas_vindas

    def apresentacao(self):
        return self.__apresentacao

    def despedida(self):
        return self.__despedida


class Bot:
    def __init__(self, nome, cumprimentos: Cumprimento, comandos: [Comando]):
        self.__nome = nome
        self.__cumprimentos = cumprimentos
        self.__comandos = comandos

    def nome(self):
        return self.__nome

    def executa_comando(self, id: int):
        self.executa_gen(id)
        for comando in self.__comandos:
            if comando.id() == valor:
                executa_gen(comando)

    def valores_comando(self, comando: Comando):
        self.generic_speech(comando.mensagem())

    def apresentacao(self):
        apresentacao = self.__cumprimentos.apresentacao()
        self.generic_speech(apresentacao)

    def boas_vindas(self):
        boas_vindas = self.__cumprimentos.boas_vindas()
        self.generic_speech(boas_vindas)

    def despedida(self):
        despedida = self.__cumprimentos.despedida()
        self.generic_speech(despedida)

    def generic_speech(self, string):
        print(f"{self.__nome}: {string}")

    def mostra_comandos(self):
        for comando in self.__comandos:
            print(f"{comando.id()}: {comando.mensagem()}")



def main():
    bot1 = Bot("bot1", Cumprimento("E ai", "Bem Vindo", "Tchau"), [Comando(2, "feliz", ["contente"])])
    novo = SistemaChatBot([bot1])
    novo.inicio()


if __name__ == "__main__":
    main()
