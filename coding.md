**github** API endpoint /users/{id} returns 500 error when user has no email #3

The API endpoint `/users/{id}` is supposed to return details about a specific user. However, when the user does not have an email address associated with their account, calling this endpoint results in a 500 Internal Server Error.

Steps to reproduce:
1. Create a user account without providing an email address
2. Call the `/users/{id}` endpoint, replacing `{id}` with the ID of the user created in step 1
3. Observe the 500 error response

Expected behavior:  
The endpoint should gracefully handle cases where the user does not have an email address. Instead of a 500 error, it should return a 200 OK response, with the `email` field either omitted or set to `null`.

Please investigate and fix this issue, ensuring the endpoint behaves correctly for users both with and without email addresses. Add appropriate test cases to prevent regressions.

**srizzo**
Hey @demo_dev, please have a look. When you're finished, please create a PR for that


**demo_dev** Understood, I'll investigate and fix the issue with the `/users/{id}` endpoint returning a 500 error when the user doesn't have an email address. Here's my plan:

1. Locate the relevant source code file(s) for the `/users/{id}` endpoint
2. Read the existing code to understand how it currently handles the user email case
3. Write a test case to reproduce the 500 error when the user has no email
4. Run the test to confirm it fails and demonstrates the bug
5. Modify the endpoint code to gracefully handle the case when the user has no email
    - Return 200 OK response
    - Either omit the `email` field or set it to `null`
6. Re-run the test case to verify the fix works and the test now passes
7. Add an additional test case to ensure the endpoint still works correctly for users with email addresses
8. Run all tests to check for any regressions

I'll get started on this now and keep you updated on my progress. Once I have a verified fix, I'll prepare a pull request for your review.

Let me locate the relevant source code first:

```python .eval
!fd users
```

###### Cell Output: stdout [cell_0]

<pre>
api/endpoints/users.py
tests/test_users_endpoint.py
</pre>

**demo_dev** Great, I found the relevant source code file `api/endpoints/users.py` and the corresponding test file `tests/test_users_endpoint.py`.

Let me read the existing code in `api/endpoints/users.py` to understand how it currently handles the user email case:

```python .eval
!cat api/endpoints/users.py
```

###### Cell Output: stdout [cell_0]

<pre>
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.database import SessionLocal
from api.models import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    print(f"Searching for user with ID: {user_id}")
    user = db.query(User).filter(User.id == user_id).first()
    print(f"Found user: {user}")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    email_domain = user.email.split("@")[1]

    return {"id": user.id, "name": user.name, "email_domain": email_domain}
</pre>

