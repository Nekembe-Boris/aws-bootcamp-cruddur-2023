-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Nekembe', 'borispokwangeh@email', 'xerxes', 'MOCK'),
  ('Andrew Bayko', 'aminaousmanu@gmail.com', 'bayko', 'MOCK');
  --('Londo Mollari', 'borisfacade@gmail.com','londo','MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid FROM public.users WHERE users.handle = 'xerxes' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )