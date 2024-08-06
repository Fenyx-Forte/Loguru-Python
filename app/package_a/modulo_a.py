from loguru import logger


@logger.catch(
    exception=ZeroDivisionError,
    level="CRITICAL",
    message="Divisao por zero",
)
def divisao(a: int, b: int) -> float:
    logger.info("Realizando divisao de {} por {}", a, b)
    return float(a / b)
