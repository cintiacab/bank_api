from pytest import raises
from .pessoa_juridica_withdrawer_controller import PJWithdrawerController         

def test_withdraw(mocker):
    mock_repository = mocker.Mock()
    controller = PJWithdrawerController(mock_repository)
    controller.withdraw(1, 35000.00)

    mock_repository.withdraw_account.assert_called_once_with(1, 35000.00)

def test_withdraw_with_error(mocker):
    mock_repository = mocker.Mock()
    controller = PJWithdrawerController(mock_repository)
    
    with raises(Exception):
        controller.withdraw(1, 55000.00)
