import polars as pl
from loguru import logger

from app.package_a import modulo_a
from app.package_b import modulo_b
from app.utils import config_log, config_polars


def aplicando_configuracao_loguru() -> None:
    configuracao = config_log.configuracao_loguru()

    logger.configure(**configuracao)


def aplicando_configuracao_polars() -> None:
    config_polars.configuracao_polars()


def minha_aplicacao():
    logger.info("Comeco do codigo")

    a = 2
    b = 1

    c = 3
    d = 4

    e = 2
    f = 0

    g = 3
    h = 0

    modulo_a.divisao(a, b)

    modulo_b.divisao(c, d)

    modulo_a.divisao(e, f)

    modulo_b.divisao(g, h)

    logger.info("Fim do codigo")
