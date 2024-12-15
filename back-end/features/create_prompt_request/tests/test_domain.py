import pytest
from ..domain.entities import PromptRequest, PromptStatus

class TestPromptRequest:
    def test_create_prompt_request(self, valid_request_id, valid_human_prompt, valid_user_role_arn):
        prompt_request = PromptRequest.create(
            request_id=valid_request_id,
            human_prompt=valid_human_prompt,
            user_role_arn=valid_user_role_arn
        )

        assert prompt_request.request_id == valid_request_id
        assert prompt_request.human_prompt == valid_human_prompt
        assert prompt_request.user_role_arn == valid_user_role_arn
        assert prompt_request.status == PromptStatus.PENDING
        assert prompt_request.result_url is None

    def test_prompt_request_immutability(self, valid_request_id, valid_human_prompt, valid_user_role_arn):
        prompt_request = PromptRequest.create(
            request_id=valid_request_id,
            human_prompt=valid_human_prompt,
            user_role_arn=valid_user_role_arn
        )

        with pytest.raises(AttributeError):
            prompt_request.request_id = valid_request_id