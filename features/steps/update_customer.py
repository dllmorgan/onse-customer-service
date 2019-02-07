from behave import when, then, given

from customer_service.model.customer import Customer


@when(u'I update customer "{customer_id:d}" surname to "{new_surname}"')
def update_customer(context, customer_id, new_surname):

    response = context.web_client.post(
        '/customers/update/' + str(customer_id) + '/' + new_surname)

    body = response.get_json()
    assert f"{body['surname']}" == new_surname

