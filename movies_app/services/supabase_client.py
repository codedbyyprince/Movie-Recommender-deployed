import os
from supabase import create_client,Client
from dotenv import load_dotenv
import sys

load_dotenv()

# 1. Read environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY')

# 2. Safety check (helps catch mistakes early)
if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    print(f"ERROR: Supabase credentials missing!", file=sys.stderr)
    print(f"  SUPABASE_URL: {SUPABASE_URL}", file=sys.stderr)
    print(f"  SUPABASE_ANON_KEY: {'SET' if SUPABASE_ANON_KEY else 'NOT SET'}", file=sys.stderr)
    raise RuntimeError("Supabase credentials missing. Set SUPABASE_URL and SUPABASE_ANON_KEY environment variables.")

# 3. Create supabase client only ONCE
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)