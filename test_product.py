import pytest
from products import Product

def test_create_normal_product():
    """
    Test creating a normal product with valid details.
    """
    product = Product("Example Product", 10, 100)
    assert product.name == "Example Product"
    assert product.price == 10
    assert product.quantity == 100
    assert product.active is True


def test_create_product_with_invalid_details():
    """
    Test creating a product with invalid details (empty name and negative price).
    """
    with pytest.raises(ValueError):
        Product("", -10, 100)


def test_product_quantity_zero_becomes_inactive():
    """
    Test that a product with a quantity of zero becomes inactive.
    """
    product = Product("Example Product", 10, 0)
    product.set_quantity(0)
    assert product.is_active() is False


def test_product_purchase_modifies_quantity():
    """
    Test that purchasing a quantity of a product modifies its quantity.
    """
    product = Product("Example Product", 10, 100)
    quantity = 50
    output = product.buy(quantity)
    assert product.quantity == 50


def test_buying_larger_quantity_than_exists_raises_exception():
    """
    Test that buying a larger quantity than exists raises a ValueError.
    """
    product = Product("Example Product", 10, 100)
    with pytest.raises(ValueError):
        product.buy(150)
