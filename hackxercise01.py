# from Root.pswd import real_password  #só no sistema da página msm q tem isso, aqui vou precisar inventar um pw
import sys  # ignore
import time
real_password = [4, 6, 7, 7]  # pw que inventei
sys.path.insert(0, '.')  # ignore


def check_password(password):  # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):  # se o dígito do input não é igual ao do pw
            return False
    return True  # 0.4s


def crack_password():

    password = [0, 0, 0, 0]  # vou guardar o palpite nessa var
    i, check = 0, False
    while (check == False):
        password[i] += 1
        time1 = time.time()  # guarda o horário antes de checar o pw
        check = check_password(password)  # 0.1s por letra
        time2 = time.time()  # guarda o horário depois de checar o pw
        diferenca = time2 - time1
        i = int((diferenca*10)-1)
        # se levar 0.2s por exemplo, quer dizer q o primeiro digito ta certo mas o segundo ta errado
        # entao temos que mudar o digito de índice 1 (o 2o dígito), que é (10*0.2)-1 e assim vai

    return password  # return cracked password


pw = crack_password()
print(pw)
