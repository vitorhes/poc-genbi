import pytest
from ..application.use_cases import CreatePromptRequestUseCase
from ..application.dto import CreatePromptRequestDTO

class TestCreatePromptRequestUseCase:
    def test_execute_success(self, valid_dto, mock_repository):
        use_case = CreatePromptRequestUseCase(repository=mock_repository)
        request_id = use_case.execute(valid_dto)

        assert isinstance(request_id, str)
        assert mock_repository.save_called

    def test_execute_with_empty_prompt(self, mock_repository):
        use_case = CreatePromptRequestUseCase(repository=mock_repository)
        dto = CreatePromptRequestDTO(
            human_prompt='',
            user_role_arn='arn:aws:iam::123456789012:role/test-role'
        )

        with pytest.raises(ValueError, match="Human prompt cannot be empty"):
            use_case.execute(dto)

    def test_execute_with_empty_user_role_arn(self, mock_repository):
        use_case = CreatePromptRequestUseCase(repository=mock_repository)
        dto = CreatePromptRequestDTO(
            human_prompt='test prompt',
            user_role_arn=''
        )

        with pytest.raises(ValueError, match="User role ARN cannot be empty"):
            use_case.execute(dto) 