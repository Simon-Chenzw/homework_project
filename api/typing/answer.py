from typing import List

import sqlalchemy
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from ..data import meta
from .comment import Comment
from .user import User
from .vote import VoteStatus

table = sqlalchemy.Table(
    'answer',
    meta,
    sqlalchemy.Column(
        'aid',
        sqlalchemy.INTEGER,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    ),
    sqlalchemy.Column(
        'qid',
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('question.qid'),
        nullable=False,
    ),
    sqlalchemy.Column(
        'uid',
        sqlalchemy.INTEGER,
        sqlalchemy.ForeignKey('user.uid'),
        nullable=False,
    ),
    sqlalchemy.Column(
        'text',
        sqlalchemy.TEXT,
        nullable=False,
    ),
)


class AnswerInDB(BaseModel):
    aid: int
    qid: int
    uid: int

    text: str


class Answer(AnswerInDB):
    user: User
    voteup_cnt: int
    votedown_cnt: int
    vote_status: VoteStatus
    comment: List[Comment]


class AnswerCreate(BaseModel):
    text: str
