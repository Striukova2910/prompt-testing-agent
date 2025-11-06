import pytest
from user_agent import user_simulator
from unittest.mock import MagicMock, patch

@patch('user_agent.ChatOpenAI')
def test_user_simulation_list(mock_chatopenai):
    dummy_questions = MagicMock()
    dummy_questions.invoke.return_value.content = "Hello, how are you?\nHow can i help you today?"
    mock_chatopenai.return_value = dummy_questions


    result = user_simulator('you are a person, who asks questions', 'small talk',
                            'gpt-4o', 0.5, 2)
    #assert result == dummy_questions
    assert len(result) == 2
    assert result[0] == "Hello, how are you?"
    assert result[1] == "How can i help you today?"
    mock_chatopenai.assert_called_once_with(model="gpt-4o", temperature=0.5, max_tokens=100)
    dummy_questions.invoke.assert_called_once()

