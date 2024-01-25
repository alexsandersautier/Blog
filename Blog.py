from connection import Base, engine, session
from Post import Post
from User import User

Base.metadata.create_all(engine)

def show_menu():
    print('1. Adicionar usuário\n2. Adicionar post\n3. Consultar post do usuário\n4. Sair\n> ')
    
def add_user():
    name = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    
    user = User(name=name,email=email)
    session.add(user)
    session.commit()
    print('Usuário adicionado com sucesso!')

def add_post():
    title = input("Digite o título do post: ")
    content = input("Digite o conteúdo do post: ")
    author_id = input("Digite o código do autor: ")
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
        print('Post adicionado com sucesso')
    else:
        print('Autor não encontrado verifique!')
    
def get_user_post():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"Usuário: {user.name}, E-mail: {user.email}")
        for post in user.posts:
            print(f" - Post: {post.title}, Conteúdo: {post.content}") 