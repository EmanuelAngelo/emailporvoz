import pyttsx3
import speech_recognition as speech
import smtplib
from email.message import EmailMessage

motor = pyttsx3.init()

def jarvisPobreFalar(mensagem): #converter texto em voz
    motor.say(mensagem)
    motor.runAndWait()

# jarvisPobreFalar("Por quê Emanuel é lindo?")

def jarvisPobreOuvir():
    reconhecer = speech.Recognizer()
    try:
        with speech.Microphone() as microfone:
            print("Estou ouvindo você.")
            audio = reconhecer.listen(microfone)
            texto = reconhecer.recognize_google(audio, language="pt-BR")
            print(texto)
            return texto.lower()
    except:
        pass
#jarvisPobreOuvir()

def jarvisPobreEnviarEmail(destino, assunto, mensagem):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('seuemail@gmail.com', 'seusenha')
    email = EmailMessage()
    email['From'] = 'seuemail@gmail.com'
    email['To'] = destino
    email['Subject'] = assunto
    email.set_content(mensagem)
    server.send_message(email)
    print("E-mail enviado com sucesso!")

def main():
    jarvisPobreFalar("Olá, vamos começar.")
    jarvisPobreFalar("Olá, irei imprimir sua lista de e-mail.")

    lista_email = {
        'mãe': 'mdas71@icloud.com',
        'namorada': 'silvaniacoutinho19@gmail.com',
        'paulo': 'pumbadeveloper@gmail.com'
    }

    print(lista_email)
    jarvisPobreFalar("Para quem voce deseja enviar este e-mail?")
    contato = jarvisPobreOuvir()

    try:
        if lista_email[contato]:
            jarvisPobreFalar(f"Qual assunto, voce deseja enviar para {lista_email[contato]} ?")
            assunto = jarvisPobreOuvir()

            jarvisPobreFalar("qual mensagem ?")
            mensagem = jarvisPobreOuvir()

            if contato and assunto and mensagem:
                jarvisPobreEnviarEmail(lista_email[contato], assunto, mensagem)
    except:
        jarvisPobreFalar("Desculpe, ocorreu um erro. Tente novamente")

main()