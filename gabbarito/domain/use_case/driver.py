from gabbarito.infra.driver import close_driver_infra, get_driver_infra


def get_driver_use_case():
    """Use case to get the driver instance.

    Returns:
        The driver instance.
    """
    return get_driver_infra()


def close_driver_use_case(driver) -> None:
    """Use case to close the driver instance.

    Args:
        driver: The driver instance to close.

    Returns:
        None
    """
    close_driver_infra(driver)
