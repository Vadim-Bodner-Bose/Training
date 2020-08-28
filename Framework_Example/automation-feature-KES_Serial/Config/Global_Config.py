
# Jira Xray Configuration
URL = 'https://jira.keurig.com'
AUTH = ("S-keurigsqa", "XK7JN!sn*kA{6y>M")

# Xray Scope Configuration

# Ayla OTA Update
TEST_PLAN_AYLA_OTA = ("TM-2000", "[Automation] Kpremium - Ayla OTA update for One brewer")
# Azure OTA Update
TEST_PLAN_KDUO_OTA = ("TM-2053", "[Automation] Kduo - Azure OTA update for One brewer")
# E2E Smoke Test Plan
TEST_PLAN_E2E_SMOKE = ("KP-23169", "E2e Mobile Daily Smoke Test")
# KES Regression Test Plan
TEST_PLAN_KES_REGRESSION = ("TM-3107", "KES auto test temp regression")
# KES Smoke Test Plan
TEST_PLAN_KES_SMOKE = ("TM-2075", "KES Daily Smoke Test for automation")
# E2E Smoke Test Plan from TM Test Plan
TEST_PLAN_E2E_SMOKE_TM = ("TM-3364", "Premium - Daily TM E2E Smoke Test Plan")
# AFH AUTOMATION
TEST_PLAN_AFH_SMOKE = ("TM-3565", "Test automation test plan")


# Test scope configuration
TEST_SCOPE = {
    "ayla_ota": TEST_PLAN_AYLA_OTA,
    "kduo_ota": TEST_PLAN_KDUO_OTA,
    "e2e_smoke": TEST_PLAN_E2E_SMOKE,
    "kes_reg": TEST_PLAN_KES_REGRESSION,
    "kes_smoke": TEST_PLAN_KES_SMOKE,
    "e2e_smoke_TM": TEST_PLAN_E2E_SMOKE_TM,
    "afh_smoke": TEST_PLAN_AFH_SMOKE,
    "example": ("TM-3179", "Test summary")   # Will be removed
}

