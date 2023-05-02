class SistemaChatBot:
    def __init__(self, lista_bots):
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots = lista_bots
        self.__bot: Bot = None
        self.__nome = "Os chifres fazem o homem, Yoda, ..."

    def escolhe_bot(self):
        print("Escolha um Bot: (1) Feliz, (2) Triste, (3) Zangado")
        print(f"{self.__nome}")
        chifres = {
            4: f"Um homem sem chifres é um animal indefeso",
            5: f"Somente um chifre pode te defender...",
            6: f"O que separa os homens dos meninos é a quantidade de chifres",
            7: "Você é muito corno..."
        }
        bot_num = int(input())
        if bot_num == 1:
            self.__bot = BotFeliz(self.__nome, {})
        elif bot_num == 2:
            self.__bot = BotTriste(self.__nome, {})
        elif bot_num == 3:
            self.__bot = BotZangado(self.__nome, chifres)
        else:
            nome = input("Nome do Bot:")
            self.__bot = Bot(nome, {})
        self.mostra_comandos_bot()

    def mostra_comandos_bot(self):
        print("1. Bom dia, como vai a sua tia?\n"
              "2. Apresentações corníferas\n"
              "3. Tchau")

    def le_envia_comando(self, comando):
        self.__bot.executa_comando(comando)

    def inicio(self):
        self.escolhe_bot()
        comando = int(input("Coloque aqui o comando\n"))
        while comando != -1:
            self.mostra_comandos_bot()
            self.le_envia_comando(comando)
            if comando == 3:self.escolhe_bot()
            comando = int(input("Coloque aqui o comando"))


class Bot:
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.comandos = comandos

    def executa_comando(self, comando: int):
        if comando == 1:
            self.apresentacao()
        elif comando == 2:
            self.boas_vindas()
        elif comando == 3:
            self.despedida()
        else:
            self.executa_gen(comando)

    def executa_gen(self, valor):
        result = self.comandos[valor]
        self.generic_speech(result)

    def apresentacao(self, string):
        self.generic_speech(string)

    def boas_vindas(self, string):
        self.generic_speech(string)

    def despedida(self, string):
        self.generic_speech(string)

    def generic_speech(self, string):
        print(f"{self.__nome}: {string}")


class BotFeliz(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)

    def apresentacao(self):
        super().apresentacao("Eu sou um Yoda Feliz")

    def boas_vindas(self):
        super().boas_vindas("Sou Feliz seu corninho manso")

    def despedida(self):
        super().despedida("Tchau corno!!!")


class BotTriste(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)

    def apresentacao(self):
        super().apresentacao("Eu sou um Yoda Bad Vibes")

    def boas_vindas(self):
        super().boas_vindas("Sou corno seu corninho manso")

    def despedida(self):
        super().despedida("Tchau corno triste!!!")


class BotZangado(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)

    def apresentacao(self):
        super().apresentacao("Vá à merda")

    def boas_vindas(self):
        super().boas_vindas("Sua mãe precisa de receita pra fazer gelo")

    def despedida(self):
        super().despedida("Sua mãe é tão velha tão velha que a certidão de nascimento passou da data de validade")


def main():
    novo = SistemaChatBot([])
    novo.inicio()


if __name__ == "__main__":
    main()
