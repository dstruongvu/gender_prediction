import pendulum, datetime


def get_current_vn_time(f_mat="%Y-%m-%d %H:%M:%S"):
    local_tz = pendulum.timezone("Asia/Bangkok")

    return datetime.now(local_tz).strftime(f_mat)

