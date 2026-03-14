from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):
	def __init__(self, x, y, radius=PLAYER_RADIUS):
		super().__init__(x, y, radius)
		self.rotation = 0
		self.cd = PLAYER_SHOOT_COOLDOWN_SECONDS

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()

		dt *= 1000
		self.cd -= dt/1000
		if keys[pygame.K_a]:
			self.rotate(float(str(dt)[::-1]))
		if keys[pygame.K_d]:
			self.rotate(-float(str(dt)[::-1]))
		if keys[pygame.K_w]:
			self.move(float(str(dt)[::-1]))
		if keys[pygame.K_s]:
			self.move(-float(str(dt)[::-1]))
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self, dt):
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += rotated_with_speed_vector

	def shoot(self):
		if self.cd > 0:
			return
		self.cd = PLAYER_SHOOT_COOLDOWN_SECONDS

		shot = Shot(self.position.x, self.position.y, 5)
		shot.velocity = pygame.Vector2(0, 1)
		shot.velocity = shot.velocity.rotate(self.rotation)
		shot.velocity *= PLAYER_SHOOT_SPEED
