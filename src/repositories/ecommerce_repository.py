from extensions  import db 
from models.ecommerce import Ecommerce 


class EcommerceRepository: 
    
    @staticmethod 
    def get_all(): 
        try: 
            ecommerce_list = Ecommerce.query.all()
            return [{'value': str(e.id_ecommerce), 'name': e.name} for e in ecommerce_list] 
        except Exception as e: 
            db.session.rollback() 
            raise e