--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: building; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.building (
    buildingname character varying(50) NOT NULL
);


ALTER TABLE public.building OWNER TO postgres;

--
-- Name: reservations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservations (
    roomnumber character varying(8) NOT NULL,
    buildingname character varying(50) NOT NULL,
    starttime time without time zone,
    endtime time without time zone
);


ALTER TABLE public.reservations OWNER TO postgres;

--
-- Name: room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.room (
    roomnumber character varying(8) NOT NULL,
    pop integer,
    roomstate integer,
    roomdescription character varying(255),
    buildingname character varying(50) NOT NULL
);


ALTER TABLE public.room OWNER TO postgres;

--
-- Name: tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tags (
    roomnumber character varying(8) NOT NULL,
    buildingname character varying(50) NOT NULL,
    tagname character varying(15)
);


ALTER TABLE public.tags OWNER TO postgres;

--
-- Data for Name: building; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.building (buildingname) FROM stdin;
\.


--
-- Data for Name: reservations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservations (roomnumber, buildingname, starttime, endtime) FROM stdin;
\.


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.room (roomnumber, pop, roomstate, roomdescription, buildingname) FROM stdin;
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tags (roomnumber, buildingname, tagname) FROM stdin;
\.


--
-- Name: building building_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.building
    ADD CONSTRAINT building_pkey PRIMARY KEY (buildingname);


--
-- Name: reservations reservations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservations
    ADD CONSTRAINT reservations_pkey PRIMARY KEY (roomnumber, buildingname);


--
-- Name: room room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (roomnumber, buildingname);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (roomnumber, buildingname);


--
-- Name: reservations reservations_roomnumber_buildingname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservations
    ADD CONSTRAINT reservations_roomnumber_buildingname_fkey FOREIGN KEY (roomnumber, buildingname) REFERENCES public.room(roomnumber, buildingname);


--
-- Name: room room_buildingname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_buildingname_fkey FOREIGN KEY (buildingname) REFERENCES public.building(buildingname);


--
-- Name: tags tags_roomnumber_buildingname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_roomnumber_buildingname_fkey FOREIGN KEY (roomnumber, buildingname) REFERENCES public.room(roomnumber, buildingname);


--
-- PostgreSQL database dump complete
--

