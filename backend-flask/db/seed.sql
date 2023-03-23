-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('sergi','gloria.macia@roche.com' , 'sergimichael' ,'MOCK'),
  ('Gloria Macia', 'gloriamaciamunoz@gmail.com','gloriamacia','MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'gloriamacia' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )