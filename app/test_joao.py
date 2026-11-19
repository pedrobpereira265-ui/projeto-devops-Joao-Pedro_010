from app import app


def test_inicio_mostra_texto_do_projeto():
    resposta = app.test_client().get("/")
    assert resposta.status_code == 200
    assert resposta.get_data(as_text=True) == "Projeto DevOps funcionando!"
