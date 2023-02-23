from wallet import Wallet

def test_getBalance():
    obj = Balance()
    obj.setBalance(20)
    assert(obj.getBalance() == 20)
