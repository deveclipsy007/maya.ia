create table if not exists patients (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  cpf text unique not null,
  phone text not null,
  email text,
  created_at timestamptz default now()
);

create table if not exists doctors (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  crm text not null,
  specialty text,
  price_cents integer not null default 0,
  is_approved boolean default false,
  is_available boolean default true
);

create table if not exists appointments (
  id uuid primary key default gen_random_uuid(),
  patient_id uuid references patients(id) on delete cascade,
  doctor_id uuid references doctors(id) on delete cascade,
  starts_at timestamptz not null,
  status text not null default 'awaiting_payment',
  price_cents integer not null default 0,
  meeting_url text,
  created_at timestamptz default now()
);

create table if not exists payments (
  id uuid primary key default gen_random_uuid(),
  appointment_id uuid references appointments(id) on delete cascade,
  provider text not null,
  status text not null,
  external_id text,
  amount_cents integer not null default 0,
  created_at timestamptz default now()
);

create table if not exists documents (
  id uuid primary key default gen_random_uuid(),
  appointment_id uuid references appointments(id) on delete cascade,
  kind text not null,
  url text not null,
  created_at timestamptz default now()
);

create table if not exists interaction_logs (
  id bigserial primary key,
  trace_id text,
  actor text,
  action text,
  payload jsonb,
  created_at timestamptz default now()
);
