from Blog import show_menu, add_post, add_user, get_user_post

while True:
    show_menu()
    option = input('Selecione uma opção: ')

    if option == '1':
        add_user()
    elif option == '2':
        add_post()
    elif option == '3':
        get_user_post()
    elif option == '4':
        break
    else:
        print("Opção inválida! Tente de 1 a 4")