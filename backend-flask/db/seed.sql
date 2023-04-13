-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('sergi','gloria.macia@roche.com' , 'sergimichael' ,'b1083e2b-32c2-4fe2-a43e-4c2bda0d9cc1'),
  ('Gloria Macia', 'gloriamaciamunoz@gmail.com','gloriamacia','78b6d613-d820-4ff2-8565-649db09d1fd3'),
  ('Londo Mollari','lmollari@centari.com' ,'londo' ,'340073c9-9c9a-4161-9325-456dec6ebda9');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'gloriamacia' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )