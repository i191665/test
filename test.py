from wallet import Wallet

def test_get_balance():
    obj = Wallet()
    obj.add_balance(20)
    assert(obj.get_balance() == 20)
