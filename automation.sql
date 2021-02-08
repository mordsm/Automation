--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO moshe;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO moshe;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO moshe;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO moshe;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO moshe;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO moshe;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO moshe;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO moshe;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO moshe;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO moshe;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO moshe;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO moshe;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO moshe;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO moshe;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO moshe;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO moshe;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO moshe;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO moshe;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO moshe;

--
-- Name: selenium_convertor_choice; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.selenium_convertor_choice (
    id integer NOT NULL,
    choice_text character varying(200) NOT NULL,
    votes integer NOT NULL,
    question_id integer NOT NULL
);


ALTER TABLE public.selenium_convertor_choice OWNER TO moshe;

--
-- Name: selenium_convertor_choice_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.selenium_convertor_choice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.selenium_convertor_choice_id_seq OWNER TO moshe;

--
-- Name: selenium_convertor_choice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.selenium_convertor_choice_id_seq OWNED BY public.selenium_convertor_choice.id;


--
-- Name: selenium_convertor_question; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.selenium_convertor_question (
    id integer NOT NULL,
    question_text character varying(200) NOT NULL,
    pub_date timestamp with time zone NOT NULL
);


ALTER TABLE public.selenium_convertor_question OWNER TO moshe;

--
-- Name: selenium_convertor_question_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.selenium_convertor_question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.selenium_convertor_question_id_seq OWNER TO moshe;

--
-- Name: selenium_convertor_question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.selenium_convertor_question_id_seq OWNED BY public.selenium_convertor_question.id;


--
-- Name: voice_chat_config; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.voice_chat_config (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    code character varying(30) NOT NULL,
    password text NOT NULL,
    data jsonb
);


ALTER TABLE public.voice_chat_config OWNER TO moshe;

--
-- Name: voice_chat_config_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.voice_chat_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voice_chat_config_id_seq OWNER TO moshe;

--
-- Name: voice_chat_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.voice_chat_config_id_seq OWNED BY public.voice_chat_config.id;


--
-- Name: voice_chat_sites; Type: TABLE; Schema: public; Owner: moshe
--

CREATE TABLE public.voice_chat_sites (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    script text NOT NULL,
    tree_script text NOT NULL,
    site_yaml text NOT NULL
);


ALTER TABLE public.voice_chat_sites OWNER TO moshe;

--
-- Name: voice_chat_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: moshe
--

CREATE SEQUENCE public.voice_chat_sites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voice_chat_sites_id_seq OWNER TO moshe;

--
-- Name: voice_chat_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: moshe
--

ALTER SEQUENCE public.voice_chat_sites_id_seq OWNED BY public.voice_chat_sites.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: selenium_convertor_choice id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.selenium_convertor_choice ALTER COLUMN id SET DEFAULT nextval('public.selenium_convertor_choice_id_seq'::regclass);


--
-- Name: selenium_convertor_question id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.selenium_convertor_question ALTER COLUMN id SET DEFAULT nextval('public.selenium_convertor_question_id_seq'::regclass);


--
-- Name: voice_chat_config id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.voice_chat_config ALTER COLUMN id SET DEFAULT nextval('public.voice_chat_config_id_seq'::regclass);


--
-- Name: voice_chat_sites id; Type: DEFAULT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.voice_chat_sites ALTER COLUMN id SET DEFAULT nextval('public.voice_chat_sites_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add question	1	add_question
2	Can change question	1	change_question
3	Can delete question	1	delete_question
4	Can view question	1	view_question
5	Can add choice	2	add_choice
6	Can change choice	2	change_choice
7	Can delete choice	2	delete_choice
8	Can view choice	2	view_choice
9	Can add sites	3	add_sites
10	Can change sites	3	change_sites
11	Can delete sites	3	delete_sites
12	Can view sites	3	view_sites
13	Can add log entry	4	add_logentry
14	Can change log entry	4	change_logentry
15	Can delete log entry	4	delete_logentry
16	Can view log entry	4	view_logentry
17	Can add permission	5	add_permission
18	Can change permission	5	change_permission
19	Can delete permission	5	delete_permission
20	Can view permission	5	view_permission
21	Can add group	6	add_group
22	Can change group	6	change_group
23	Can delete group	6	delete_group
24	Can view group	6	view_group
25	Can add user	7	add_user
26	Can change user	7	change_user
27	Can delete user	7	delete_user
28	Can view user	7	view_user
29	Can add content type	8	add_contenttype
30	Can change content type	8	change_contenttype
31	Can delete content type	8	delete_contenttype
32	Can view content type	8	view_contenttype
33	Can add session	9	add_session
34	Can change session	9	change_session
35	Can delete session	9	delete_session
36	Can view session	9	view_session
37	Can add config	10	add_config
38	Can change config	10	change_config
39	Can delete config	10	delete_config
40	Can view config	10	view_config
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	selenium_convertor	question
2	selenium_convertor	choice
3	voice_chat	sites
4	admin	logentry
5	auth	permission
6	auth	group
7	auth	user
8	contenttypes	contenttype
9	sessions	session
10	voice_chat	config
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-09-08 10:31:10.663062+03
2	auth	0001_initial	2020-09-08 10:31:10.725953+03
3	admin	0001_initial	2020-09-08 10:31:10.809884+03
4	admin	0002_logentry_remove_auto_add	2020-09-08 10:31:10.828708+03
5	admin	0003_logentry_add_action_flag_choices	2020-09-08 10:31:10.83873+03
6	contenttypes	0002_remove_content_type_name	2020-09-08 10:31:10.873892+03
7	auth	0002_alter_permission_name_max_length	2020-09-08 10:31:10.886715+03
8	auth	0003_alter_user_email_max_length	2020-09-08 10:31:10.898755+03
9	auth	0004_alter_user_username_opts	2020-09-08 10:31:10.908955+03
10	auth	0005_alter_user_last_login_null	2020-09-08 10:31:10.918875+03
11	auth	0006_require_contenttypes_0002	2020-09-08 10:31:10.922761+03
12	auth	0007_alter_validators_add_error_messages	2020-09-08 10:31:10.933799+03
13	auth	0008_alter_user_username_max_length	2020-09-08 10:31:10.951547+03
14	auth	0009_alter_user_last_name_max_length	2020-09-08 10:31:10.961649+03
15	auth	0010_alter_group_name_max_length	2020-09-08 10:31:10.972788+03
16	auth	0011_update_proxy_permissions	2020-09-08 10:31:10.980993+03
17	auth	0012_alter_user_first_name_max_length	2020-09-08 10:31:10.990742+03
18	selenium_convertor	0001_initial	2020-09-08 10:31:11.005889+03
19	sessions	0001_initial	2020-09-08 10:31:11.02293+03
22	voice_chat	0001_initial	2020-10-14 17:40:56.521926+03
23	voice_chat	0002_sites_tree_script	2020-10-14 17:40:56.547639+03
24	voice_chat	0003_sites_site_yaml	2020-10-14 17:40:56.55561+03
25	voice_chat	0004_config	2020-12-16 10:00:11.486503+02
26	voice_chat	0005_auto_20201216_0805	2020-12-16 10:05:16.922698+02
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
yey3d75weuzgboztookjdhx6zej3rcyu	e30:1kQc6u:FnchCyJZC5GC2TVNDn7hyBl4CE2FR9dkzP091B0yCgI	2020-10-22 23:01:56.589127+03
\.


--
-- Data for Name: selenium_convertor_choice; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.selenium_convertor_choice (id, choice_text, votes, question_id) FROM stdin;
\.


--
-- Data for Name: selenium_convertor_question; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.selenium_convertor_question (id, question_text, pub_date) FROM stdin;
\.


--
-- Data for Name: voice_chat_config; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.voice_chat_config (id, name, code, password, data) FROM stdin;
5	bankhapoalim	vn02727	mordsmi9	\N
6	email	sharon.moshe@gmail.com	mordsmi4	\N
\.


--
-- Data for Name: voice_chat_sites; Type: TABLE DATA; Schema: public; Owner: moshe
--

COPY public.voice_chat_sites (id, name, script, tree_script, site_yaml) FROM stdin;
4	בנק הפועלים		{\n  "בנק הפועלים": [\n    {\n      "name": "login",\n      "commands": [\n        {\n          "id": "c153076a-8beb-499c-ade7-89837b664130",\n          "comment": "",\n          "command": "open",\n          "target": "https://www.bankhapoalim.co.il/he/login",\n          "targets": [],\n          "value": "",\n          "name": "כניסה לחשבונך - בנק הפועלים",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "b664752e-9eaf-4c2c-b946-e813561b79aa",\n          "comment": "",\n          "command": "setWindowSize",\n          "target": "1717x1100",\n          "targets": [],\n          "value": "",\n          "name": "",\n          "title": "\\\\u05db\\\\u05e0\\\\u05d9\\\\u05e1\\\\u05d4 \\\\u05dc\\\\u05d7\\\\u05le9\\\\u05d1\\\\u05d5\\\\u05e0\\\\u05da - \\\\u05d1\\\\u05e0\\\\u05e7 \\\\u05d4\\\\u05e4\\\\u05d5\\\\u05e2\\\\u05dc\\\\u05d9\\\\u05dd"\n        },\n        {\n          "id": "496273d4-f96e-4765-abdc-4b0c11999e4e",\n          "comment": "",\n          "command": "click",\n          "target": "css=.login-button > .desktop",\n          "targets": [\n            [\n              "css=.login-button > .desktop",\n              "css:finder"\n            ],\n            [\n              "xpath=//li[2]/a/span",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "commands": {},\n          "name": "כניסה לחשבון",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "3d9d1a8e-576e-4c77-8339-44c909f91943",\n          "comment": "",\n          "command": "selectFrame",\n          "target": "index=0",\n          "targets": [\n            [\n              "index=0"\n            ]\n          ],\n          "value": "",\n          "name": "",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "82e1ebf4-0f4f-4d27-9299-a188f6305856",\n          "comment": "",\n          "command": "click",\n          "target": "id=userCode",\n          "targets": [\n            [\n              "id=userCode",\n              "id"\n            ],\n            [\n              "css=#userCode",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='userCode']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//input",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "קוד משתמש",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "32b2761d-a819-40e5-aba3-167a9306ab5e",\n          "comment": "",\n          "command": "type",\n          "target": "id=userCode",\n          "targets": [\n            [\n              "id=userCode",\n              "id"\n            ],\n            [\n              "css=#userCode",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='userCode']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//input",\n              "xpath:position"\n            ]\n          ],\n          "value": "vn02727",\n          "name": "קוד משתמש",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "78f318cf-65ff-4324-a1bb-fd3ff0546c41",\n          "comment": "",\n          "command": "click",\n          "target": "id=password",\n          "targets": [\n            [\n              "id=password",\n              "id"\n            ],\n            [\n              "css=#password",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='password']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//div[2]/poalim-mm-field/div/input",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "סיסמה",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "b8ee6f98-3b94-43aa-93ef-0b08c2e57c8c",\n          "comment": "",\n          "command": "type",\n          "target": "id=password",\n          "targets": [\n            [\n              "id=password",\n              "id"\n            ],\n            [\n              "css=#password",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='password']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//div[2]/poalim-mm-field/div/input",\n              "xpath:position"\n            ]\n          ],\n          "value": "mordsmi9",\n          "name": "סיסמה",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "23cfaccf-dfbe-4230-ba36-ea8c33dec81f",\n          "comment": "",\n          "command": "click",\n          "target": "css=.red-coloring-btn",\n          "targets": [\n            [\n              "css=.red-coloring-btn",\n              "css:finder"\n            ],\n            [\n              "xpath=//button[@type='submit']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//div[3]/button",\n              "xpath:position"\n            ],\n            [\n              "xpath=//button[contains(.,'כניסה')]",\n              "xpath:innerText"\n            ]\n          ],\n          "value": "",\n          "name": "כניסה",\n          "title": "דף הבית"\n        }\n      ]\n    },\n    {\n      "name": "בחר חשבון",\n      "commands": [\n        {\n          "id": "32e274b7-ada2-4643-bec0-f1021c3f1e34",\n          "comment": "",\n          "command": "click",\n          "target": "id=rb-accounts-filter-0",\n          "targets": [\n            [\n              "id=rb-accounts-filter-0",\n              "id"\n            ],\n            [\n              "css=#rb-accounts-filter-0",\n              "css:finder"\n            ],\n            [\n              "xpath=//button[@id='rb-accounts-filter-0']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//section[@id='toolbar']/poalim-accounts-filter/div/button",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//poalim-accounts-filter/div/button",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "מס' : 91-15596",\n          "title": "דף הבית"\n        },\n        {\n          "id": "ec71af4b-be96-4a13-85cf-300069304f0b",\n          "comment": "",\n          "command": "click",\n          "target": "css=.account-item:nth-child(3) > label",\n          "targets": [\n            [\n              "css=.account-item:nth-child(3) > label",\n              "css:finder"\n            ],\n            [\n              "xpath=//ul[@id='rb-accounts-filter-0-account-list']/li[3]/label",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//li[3]/label",\n              "xpath:position"\n            ],\n            [\n              "xpath=//label[contains(.,'91-396646')]",\n              "xpath:innerText"\n            ]\n          ],\n          "value": "",\n          "name": "",\n          "title": "דף הבית"\n        }\n      ]\n    },\n    {\n      "name": "עובר ושב",\n      "commands": [\n        {\n          "id": "0aa25f03-28f9-4f1d-a19c-5cc6488b983b",\n          "comment": "",\n          "command": "click",\n          "target": "id=mega-menu-1",\n          "targets": [\n            [\n              "id=mega-menu-1",\n              "id"\n            ],\n            [\n              "css=#mega-menu-1",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[@id='mega-menu-1']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//nav[@id='main-nav']/ul/li[2]/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//a[contains(@href, '/ng-portals/rb/he/current-account')]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//li[2]/a",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "עובר\\nושב",\n          "title": "תנועות בחשבון"\n        }\n      ]\n    },\n    {\n      "name": "תנועות עתידיות",\n      "commands": [\n        {\n          "id": "a788e541-c3ce-4d33-8420-c06f4334c3a2",\n          "comment": "",\n          "command": "click",\n          "target": "linkText=תנועות עתידיות",\n          "targets": [\n            [\n              "linkText=תנועות עתידיות",\n              "linkText"\n            ],\n            [\n              "css=.card-body li:nth-child(2) > a",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[contains(text(),'תנועות עתידיות')]",\n              "xpath:link"\n            ],\n            [\n              "xpath=//div[@id='currentAccountInfoAndTransactions']/div/ul/li[2]/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//a[contains(@href, '/ng-portals-bt/rb/he/current-account/future-transactions')]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//div[2]/div/ul/li[2]/a",\n              "xpath:position"\n            ],\n            [\n              "xpath=//a[contains(.,'תנועות עתידיות')]",\n              "xpath:innerText"\n            ]\n          ],\n          "value": "",\n          "name": "תנועות עתידיות",\n          "title": "תנועות עתידיות"\n        }\n      ]\n    },\n    {\n      "name": "Home",\n      "commands": [\n        {\n          "id": "a788e541-c3ce-4d33-8420-c06f4334c3a2",\n          "comment": "",\n          "command": "click",\n          "target": "id=mega-menu-0",\n          "targets": [\n            [\n              "id=mega-menu-0",\n              "id"\n            ],\n            [\n              "css=#mega-menu-0",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[@id='mega-menu-0']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//nav[@id='main-nav']/ul/li/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=(//a[contains(@href, '/ng-portals/rb/he/homepage')])[2]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//li/a",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "Home",\n          "title": "Home"\n        }\n      ]\n    },\n    {\n      "commands": [\n        {\n          "id": "44531362-8805-429a-a0c0-dd5b7c66d93a",\n          "comment": "",\n          "command": "click",\n          "target": "id=mega-menu-8",\n          "targets": [\n            [\n              "id=mega-menu-8",\n              "id"\n            ],\n            [\n              "css=#mega-menu-8",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[@id='mega-menu-8']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//nav[@id='main-nav']/ul/li[9]/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//a[contains(@href, '/ng-portals/rb/he/pfm')]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//li[9]/a",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "title": "ניהול תקציבי"\n        }\n      ],\n      "name": "ניהול תקציב"\n    }\n  ]\n}	בנק הפועלים:\n    בחר חשבון:\n        עובר ושב:\n            - תנועות עתידיות:\n            - תנועות בחשבון:\n            - ריכוז יתרות:\n        לאתר שוק ההון:\n            פיקדונות וחסכונות:\n            - מידע:\n            - פר"י:\n            - פקדונות שקליים:\n        תשלומי חשבונות:\n            - חשבון חשמל:\n            - רשויות מקומיות:\n        מטבע חוץ :\n            - תנועות מט"ח:\n            - שערי מט"ח:\n        כרטיסי אשראי:\n            - חיובים קרובים:\n            - חיובים קודמים:\n        ניהול תקציב:\n\n
5	bankhapoalim		{\n  "בנק הפועלים": [\n    {\n      "name": "login",\n      "commands": [\n        {\n          "id": "c153076a-8beb-499c-ade7-89837b664130",\n          "comment": "",\n          "command": "open",\n          "target": "https://www.bankhapoalim.co.il/he/login",\n          "targets": [],\n          "value": "",\n          "name": "כניסה לחשבונך - בנק הפועלים",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "b664752e-9eaf-4c2c-b946-e813561b79aa",\n          "comment": "",\n          "command": "setWindowSize",\n          "target": "1717x1100",\n          "targets": [],\n          "value": "",\n          "name": "",\n          "title": "\\\\u05db\\\\u05e0\\\\u05d9\\\\u05e1\\\\u05d4 \\\\u05dc\\\\u05d7\\\\u05le9\\\\u05d1\\\\u05d5\\\\u05e0\\\\u05da - \\\\u05d1\\\\u05e0\\\\u05e7 \\\\u05d4\\\\u05e4\\\\u05d5\\\\u05e2\\\\u05dc\\\\u05d9\\\\u05dd"\n        },\n        {\n          "id": "496273d4-f96e-4765-abdc-4b0c11999e4e",\n          "comment": "",\n          "command": "click",\n          "target": "css=.login-button > .desktop",\n          "targets": [\n            [\n              "css=.login-button > .desktop",\n              "css:finder"\n            ],\n            [\n              "xpath=//li[2]/a/span",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "commands": {},\n          "name": "כניסה לחשבון",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "3d9d1a8e-576e-4c77-8339-44c909f91943",\n          "comment": "",\n          "command": "selectFrame",\n          "target": "index=0",\n          "targets": [\n            [\n              "index=0"\n            ]\n          ],\n          "value": "",\n          "name": "",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "82e1ebf4-0f4f-4d27-9299-a188f6305856",\n          "comment": "",\n          "command": "click",\n          "target": "id=userCode",\n          "targets": [\n            [\n              "id=userCode",\n              "id"\n            ],\n            [\n              "css=#userCode",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='userCode']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//input",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "קוד משתמש",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "32b2761d-a819-40e5-aba3-167a9306ab5e",\n          "comment": "",\n          "command": "type",\n          "target": "id=userCode",\n          "targets": [\n            [\n              "id=userCode",\n              "id"\n            ],\n            [\n              "css=#userCode",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='userCode']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//input",\n              "xpath:position"\n            ]\n          ],\n          "value": "vn02727",\n          "name": "קוד משתמש",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "78f318cf-65ff-4324-a1bb-fd3ff0546c41",\n          "comment": "",\n          "command": "click",\n          "target": "id=password",\n          "targets": [\n            [\n              "id=password",\n              "id"\n            ],\n            [\n              "css=#password",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='password']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//div[2]/poalim-mm-field/div/input",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "סיסמה",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "b8ee6f98-3b94-43aa-93ef-0b08c2e57c8c",\n          "comment": "",\n          "command": "type",\n          "target": "id=password",\n          "targets": [\n            [\n              "id=password",\n              "id"\n            ],\n            [\n              "css=#password",\n              "css:finder"\n            ],\n            [\n              "xpath=//input[@id='password']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//div[2]/poalim-mm-field/div/input",\n              "xpath:position"\n            ]\n          ],\n          "value": "mordsmi9",\n          "name": "סיסמה",\n          "title": "כניסה לחשבונך - בנק הפועלים"\n        },\n        {\n          "id": "23cfaccf-dfbe-4230-ba36-ea8c33dec81f",\n          "comment": "",\n          "command": "click",\n          "target": "css=.red-coloring-btn",\n          "targets": [\n            [\n              "css=.red-coloring-btn",\n              "css:finder"\n            ],\n            [\n              "xpath=//button[@type='submit']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//div[3]/button",\n              "xpath:position"\n            ],\n            [\n              "xpath=//button[contains(.,'כניסה')]",\n              "xpath:innerText"\n            ]\n          ],\n          "value": "",\n          "name": "כניסה",\n          "title": "דף הבית"\n        }\n      ]\n    },\n    {\n      "name": "בחר חשבון",\n      "commands": [\n        {\n          "id": "32e274b7-ada2-4643-bec0-f1021c3f1e34",\n          "comment": "",\n          "command": "click",\n          "target": "id=rb-accounts-filter-0",\n          "targets": [\n            [\n              "id=rb-accounts-filter-0",\n              "id"\n            ],\n            [\n              "css=#rb-accounts-filter-0",\n              "css:finder"\n            ],\n            [\n              "xpath=//button[@id='rb-accounts-filter-0']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//section[@id='toolbar']/poalim-accounts-filter/div/button",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//poalim-accounts-filter/div/button",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "מס' : 91-15596",\n          "title": "דף הבית"\n        },\n        {\n          "id": "ec71af4b-be96-4a13-85cf-300069304f0b",\n          "comment": "",\n          "command": "click",\n          "target": "css=.account-item:nth-child(3) > label",\n          "targets": [\n            [\n              "css=.account-item:nth-child(3) > label",\n              "css:finder"\n            ],\n            [\n              "xpath=//ul[@id='rb-accounts-filter-0-account-list']/li[3]/label",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//li[3]/label",\n              "xpath:position"\n            ],\n            [\n              "xpath=//label[contains(.,'91-396646')]",\n              "xpath:innerText"\n            ]\n          ],\n          "value": "",\n          "name": "",\n          "title": "דף הבית"\n        }\n      ]\n    },\n    {\n      "name": "עובר ושב",\n      "commands": [\n        {\n          "id": "0aa25f03-28f9-4f1d-a19c-5cc6488b983b",\n          "comment": "",\n          "command": "click",\n          "target": "id=mega-menu-1",\n          "targets": [\n            [\n              "id=mega-menu-1",\n              "id"\n            ],\n            [\n              "css=#mega-menu-1",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[@id='mega-menu-1']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//nav[@id='main-nav']/ul/li[2]/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//a[contains(@href, '/ng-portals/rb/he/current-account')]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//li[2]/a",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "עובר\\nושב",\n          "title": "תנועות בחשבון"\n        }\n      ]\n    },\n    {\n      "name": "תנועות עתידיות",\n      "commands": [\n        {\n          "id": "a788e541-c3ce-4d33-8420-c06f4334c3a2",\n          "comment": "",\n          "command": "click",\n          "target": "linkText=תנועות עתידיות",\n          "targets": [\n            [\n              "linkText=תנועות עתידיות",\n              "linkText"\n            ],\n            [\n              "css=.card-body li:nth-child(2) > a",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[contains(text(),'תנועות עתידיות')]",\n              "xpath:link"\n            ],\n            [\n              "xpath=//div[@id='currentAccountInfoAndTransactions']/div/ul/li[2]/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//a[contains(@href, '/ng-portals-bt/rb/he/current-account/future-transactions')]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//div[2]/div/ul/li[2]/a",\n              "xpath:position"\n            ],\n            [\n              "xpath=//a[contains(.,'תנועות עתידיות')]",\n              "xpath:innerText"\n            ]\n          ],\n          "value": "",\n          "name": "תנועות עתידיות",\n          "title": "תנועות עתידיות"\n        }\n      ]\n    },\n    {\n      "name": "Home",\n      "commands": [\n        {\n          "id": "a788e541-c3ce-4d33-8420-c06f4334c3a2",\n          "comment": "",\n          "command": "click",\n          "target": "id=mega-menu-0",\n          "targets": [\n            [\n              "id=mega-menu-0",\n              "id"\n            ],\n            [\n              "css=#mega-menu-0",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[@id='mega-menu-0']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//nav[@id='main-nav']/ul/li/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=(//a[contains(@href, '/ng-portals/rb/he/homepage')])[2]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//li/a",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "name": "Home",\n          "title": "Home"\n        }\n      ]\n    },\n    {\n      "commands": [\n        {\n          "id": "44531362-8805-429a-a0c0-dd5b7c66d93a",\n          "comment": "",\n          "command": "click",\n          "target": "id=mega-menu-8",\n          "targets": [\n            [\n              "id=mega-menu-8",\n              "id"\n            ],\n            [\n              "css=#mega-menu-8",\n              "css:finder"\n            ],\n            [\n              "xpath=//a[@id='mega-menu-8']",\n              "xpath:attributes"\n            ],\n            [\n              "xpath=//nav[@id='main-nav']/ul/li[9]/a",\n              "xpath:idRelative"\n            ],\n            [\n              "xpath=//a[contains(@href, '/ng-portals/rb/he/pfm')]",\n              "xpath:href"\n            ],\n            [\n              "xpath=//li[9]/a",\n              "xpath:position"\n            ]\n          ],\n          "value": "",\n          "title": "ניהול תקציבי"\n        }\n      ],\n      "name": "ניהול תקציב"\n    }\n  ]\n}	בנק הפועלים:\n    בחר חשבון:\n        עובר ושב:\n            - תנועות עתידיות:\n            - תנועות בחשבון:\n            - ריכוז יתרות:\n        לאתר שוק ההון:\n            פיקדונות וחסכונות:\n            - מידע:\n            - פר"י:\n            - פקדונות שקליים:\n        תשלומי חשבונות:\n            - חשבון חשמל:\n            - רשויות מקומיות:\n        מטבע חוץ :\n            - תנועות מט"ח:\n            - שערי מט"ח:\n        כרטיסי אשראי:\n            - חיובים קרובים:\n            - חיובים קודמים:\n        ניהול תקציב:\n\n
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: selenium_convertor_choice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.selenium_convertor_choice_id_seq', 1, false);


--
-- Name: selenium_convertor_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.selenium_convertor_question_id_seq', 1, false);


--
-- Name: voice_chat_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.voice_chat_config_id_seq', 6, true);


--
-- Name: voice_chat_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moshe
--

SELECT pg_catalog.setval('public.voice_chat_sites_id_seq', 5, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: selenium_convertor_choice selenium_convertor_choice_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.selenium_convertor_choice
    ADD CONSTRAINT selenium_convertor_choice_pkey PRIMARY KEY (id);


--
-- Name: selenium_convertor_question selenium_convertor_question_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.selenium_convertor_question
    ADD CONSTRAINT selenium_convertor_question_pkey PRIMARY KEY (id);


--
-- Name: voice_chat_config voice_chat_config_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.voice_chat_config
    ADD CONSTRAINT voice_chat_config_pkey PRIMARY KEY (id);


--
-- Name: voice_chat_sites voice_chat_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.voice_chat_sites
    ADD CONSTRAINT voice_chat_sites_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: selenium_convertor_choice_question_id_2840dae2; Type: INDEX; Schema: public; Owner: moshe
--

CREATE INDEX selenium_convertor_choice_question_id_2840dae2 ON public.selenium_convertor_choice USING btree (question_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selenium_convertor_choice selenium_convertor_c_question_id_2840dae2_fk_selenium_; Type: FK CONSTRAINT; Schema: public; Owner: moshe
--

ALTER TABLE ONLY public.selenium_convertor_choice
    ADD CONSTRAINT selenium_convertor_c_question_id_2840dae2_fk_selenium_ FOREIGN KEY (question_id) REFERENCES public.selenium_convertor_question(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

