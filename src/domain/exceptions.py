class EntityAlreadyExistsError(ValueError):
    pass


class RelatedEntityNotFoundError(ValueError):
    pass


class ScheduleConflictError(ValueError):
    pass