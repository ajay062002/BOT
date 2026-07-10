# Graph Report - f1-app  (2026-07-10)

## Corpus Check
- 90 files · ~823,415 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 588 nodes · 856 edges · 40 communities (30 shown, 10 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 48 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c1367b65`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- EmailService
- LiveEvent
- DriverStat
- AppUser
- Circuit
- ChatResponse
- Driver
- Team
- app.js
- GlobalExceptionHandler.java
- F1 Live – Spring Boot F1 Portal
- Resume Builder – Student & Recruiter Portal
- AiController
- circuits.js
- mvnw
- SecurityConfig.java
- F1AppApplication
- HighlightController
- RegisterRequest
- WebConfig.java
- ViewController
- NewsletterSendRequest
- LoginRequest
- auth.js
- F1appApplicationTests.java
- ChatData
- AuthResponse
- Role
- build.sh
- github-profile-README.md
- minecraft-readme.md
- com.example:f1app

## God Nodes (most connected - your core abstractions)
1. `Circuit` - 30 edges
2. `Driver` - 29 edges
3. `DriverStat` - 29 edges
4. `AppUser` - 27 edges
5. `EmailService` - 26 edges
6. `User` - 24 edges
7. `AppUserRepository` - 22 edges
8. `Team` - 21 edges
9. `ChatResponse` - 19 edges
10. `LiveEvent` - 17 edges

## Surprising Connections (you probably didn't know these)
- `AuthController` --references--> `AppUserRepository`  [EXTRACTED]
  src/main/java/com/example/f1app/controller/AuthController.java → src/main/java/com/example/f1app/repository/AppUserRepository.java
- `AuthController` --references--> `EmailService`  [EXTRACTED]
  src/main/java/com/example/f1app/controller/AuthController.java → src/main/java/com/example/f1app/service/EmailService.java
- `AppUserRepository` --references--> `AppUser`  [EXTRACTED]
  src/main/java/com/example/f1app/repository/AppUserRepository.java → src/main/java/com/example/f1app/model/AppUser.java
- `DriverStat` --references--> `Driver`  [EXTRACTED]
  src/main/java/com/example/f1app/model/DriverStat.java → src/main/java/com/example/f1app/model/Driver.java
- `NewsletterService` --references--> `AppUserRepository`  [EXTRACTED]
  src/main/java/com/example/f1app/service/NewsletterService.java → src/main/java/com/example/f1app/repository/AppUserRepository.java

## Import Cycles
- None detected.

## Communities (40 total, 10 thin omitted)

### Community 0 - "User"
Cohesion: 0.06
Nodes (20): Autowired, RegisterRequest, CrossOrigin, GetMapping, PostMapping, RequestMapping, ResponseEntity, RestController (+12 more)

### Community 1 - "EmailService"
Cohesion: 0.06
Nodes (30): Async, JavaMailSender, Logger, AdminNewsletterController, PostMapping, RequestMapping, RestController, EmailController (+22 more)

### Community 2 - "LiveEvent"
Cohesion: 0.07
Nodes (24): HttpSession, AdminController, CrossOrigin, PostMapping, RequestMapping, ResponseEntity, RestController, CrossOrigin (+16 more)

### Community 3 - "DriverStat"
Cohesion: 0.07
Nodes (13): Query, ConstructorStanding, DriverStanding, CrossOrigin, GetMapping, RequestMapping, RestController, SeasonInfo (+5 more)

### Community 4 - "AppUser"
Cohesion: 0.07
Nodes (16): HttpServletRequest, AuthController, GetMapping, PasswordEncoder, PostMapping, RequestMapping, ResponseEntity, RestController (+8 more)

### Community 5 - "Circuit"
Cohesion: 0.06
Nodes (10): JpaRepository, CircuitController, CrossOrigin, GetMapping, RequestMapping, RestController, Circuit, Entity (+2 more)

### Community 6 - "ChatResponse"
Cohesion: 0.09
Nodes (10): SafeVarargs, ChatController, CrossOrigin, PostMapping, RequestMapping, RestController, ChatRequest, ChatResponse (+2 more)

### Community 7 - "Driver"
Cohesion: 0.07
Nodes (10): DriverController, CrossOrigin, GetMapping, PostMapping, RequestMapping, RestController, Driver, Entity (+2 more)

### Community 8 - "Team"
Cohesion: 0.08
Nodes (10): CrossOrigin, GetMapping, PostMapping, RequestMapping, RestController, TeamController, Entity, Table (+2 more)

### Community 9 - "app.js"
Cohesion: 0.19
Nodes (11): auth, getJSON(), parseRoute(), render(), routes, AdminPage, DriversPage, HomePage (+3 more)

### Community 11 - "GlobalExceptionHandler.java"
Cohesion: 0.35
Nodes (7): DataIntegrityViolationException, ExceptionHandler, HttpMessageNotReadableException, MethodArgumentNotValidException, RestControllerAdvice, GlobalExceptionHandler, ResponseEntity

### Community 12 - "F1 Live – Spring Boot F1 Portal"
Cohesion: 0.17
Nodes (11): 1. Create the database, 2. Set environment variables, 3. Run, API Endpoints, F1 Live – Spring Boot F1 Portal, Prerequisites, Project Structure, Running Locally (+3 more)

### Community 13 - "Resume Builder – Student & Recruiter Portal"
Cohesion: 0.17
Nodes (11): 1. Clone the repo, 2. Install dependencies, 3. Run migrations, 4. Start the server, Author, Features, How It Works, Login (+3 more)

### Community 14 - "AiController"
Cohesion: 0.23
Nodes (7): AiController, CrossOrigin, PostMapping, RequestMapping, RestController, Service, SummaryService

### Community 15 - "circuits.js"
Cohesion: 0.33
Nodes (10): closeModal(), computeSpeed(), openCircuit(), ovalPath(), positionCar(), renderLaps(), reset(), start() (+2 more)

### Community 16 - "mvnw"
Cohesion: 0.33
Nodes (6): mvnw script, clean(), die(), exec_maven(), set_java_home(), verbose()

### Community 17 - "SecurityConfig.java"
Cohesion: 0.39
Nodes (6): Bean, HttpSecurity, SecurityFilterChain, Configuration, PasswordEncoder, SecurityConfig

### Community 18 - "F1AppApplication"
Cohesion: 0.43
Nodes (6): EnableAsync, EnableJpaRepositories, EnableScheduling, EntityScan, SpringBootApplication, F1AppApplication

### Community 19 - "HighlightController"
Cohesion: 0.29
Nodes (6): Highlight, HighlightController, CrossOrigin, GetMapping, RequestMapping, RestController

### Community 21 - "WebConfig.java"
Cohesion: 0.43
Nodes (5): CorsRegistry, Override, Configuration, WebConfig, WebMvcConfigurer

### Community 22 - "ViewController"
Cohesion: 0.53
Nodes (3): Controller, GetMapping, ViewController

### Community 26 - "F1appApplicationTests.java"
Cohesion: 0.60
Nodes (3): SpringBootTest, F1appApplicationTests, Test

### Community 29 - "Role"
Cohesion: 0.50
Nodes (3): Role, ADMIN, USER

## Knowledge Gaps
- **26 isolated node(s):** `build.sh script`, `com.example:f1app`, `USER`, `ADMIN`, `routes` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AppUserRepository` connect `EmailService` to `User`, `AppUser`, `Circuit`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Why does `UserRepository` connect `User` to `EmailService`, `Circuit`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Why does `LiveEventRepository` connect `LiveEvent` to `Circuit`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **What connects `build.sh script`, `com.example:f1app`, `USER` to the rest of the system?**
  _26 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `User` be split into smaller, more focused modules?**
  _Cohesion score 0.06019871420222092 - nodes in this community are weakly interconnected._
- **Should `EmailService` be split into smaller, more focused modules?**
  _Cohesion score 0.06313497822931785 - nodes in this community are weakly interconnected._
- **Should `LiveEvent` be split into smaller, more focused modules?**
  _Cohesion score 0.06567992599444958 - nodes in this community are weakly interconnected._