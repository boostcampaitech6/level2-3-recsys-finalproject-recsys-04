from drf_yasg import openapi

def create_user_schema():
    return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'sex': openapi.Schema(type=openapi.TYPE_STRING, description="User sex ('M' or 'F')", default="M"),
                'age': openapi.Schema(type=openapi.TYPE_INTEGER, description="User age", default=20),
                'price': openapi.Schema(type=openapi.TYPE_INTEGER, description="UserDetail price", default=10000),
                'personality': openapi.Schema(type=openapi.TYPE_INTEGER, description="UserDetail personality", default=50),
                'category_1': openapi.Schema(type=openapi.TYPE_STRING, description="UserDetail category_1", default="개업선물"),
            },
            required=['sex', 'age', 'price', 'personality', 'category_1'],
        )