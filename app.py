from flask import Flask

from controller.target_controller import target_blueprint
from model import Target
from repository.init_database import create_table
from repository.target_repository import insert_target, delete_target, update_target

app = Flask(__name__)
if __name__ == '__main__':
    # create_table()
    # target = Target(target_priority=1, target_industry="test", city_id=2195, target_type_id=3000)
    # target = insert_target(target).unwrap()
    # target.target_industry = "test_update"
    # target = update_target(target, target.target_id).unwrap()
    # tmp = delete_target(target.target_id)
    app.register_blueprint(target_blueprint, url_prefix="/api/mission")
    app.run(debug=True)

