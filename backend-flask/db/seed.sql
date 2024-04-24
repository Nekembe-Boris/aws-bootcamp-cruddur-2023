-- this file was manually created
INSERT INTO public.users (display_name, handle, email, cognito_user_id)
VALUES
  ('Nekembe', 'Xerxes', 'borispokwangeh@email', 'MOCK'),
  ('Andrew Bayko', 'bayko', 'test@email' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid FROM public.users WHERE users.handle = 'Xerxes' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )