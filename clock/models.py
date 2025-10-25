from django.db import models

from utils.models import BaseModel


class ClockEntry(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    job = models.ForeignKey('job.Job', on_delete=models.CASCADE)
    clock_in_time = models.DateTimeField()
    clock_out_time = models.DateTimeField(null=True, blank=True)

    @property
    def duration(self):
        if not self.clock_out_time:
            return None
        delta = self.clock_out_time - self.clock_in_time
        total_seconds = int(delta.total_seconds())
        if total_seconds < 0:
            total_seconds = 0
        hours, remainder = divmod(total_seconds, 3600)
        minutes = remainder // 60
        return f"{hours}h {minutes}m"

    def __str__(self):
        return f"ClockEntry for {self.user.first_name} on {self.clock_in_time.date()}"
