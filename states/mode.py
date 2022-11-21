from  aiogram.dispatcher.filters.state import StatesGroup, State
class mode_state(StatesGroup):
    mode = State()
    in_game = State()
    end_game = State()