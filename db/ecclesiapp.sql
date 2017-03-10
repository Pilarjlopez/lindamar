-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 03-03-2017 a las 03:35:47
-- Versión del servidor: 10.1.21-MariaDB
-- Versión de PHP: 7.0.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ecclesiapp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `id_actividad` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `dia` int(11) NOT NULL,
  `hora` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `id_templo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `actividad`
--

INSERT INTO `actividad` (`id_actividad`, `nombre`, `dia`, `hora`, `descripcion`, `id_templo`) VALUES
(1, '', 0, 0, '', 1),
(2, '', 0, 0, '', 2),
(3, '', 0, 0, '', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id_categoria`, `tipo`) VALUES
(1, 'Parroquia'),
(2, 'Capilla'),
(3, 'Catedral');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id_departamento` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `nombre`) VALUES
(1, 'Managua'),
(2, 'Masaya'),
(3, 'Carazo'),
(4, 'Rivas'),
(5, 'León'),
(6, 'Chinandega');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diocesis`
--

CREATE TABLE `diocesis` (
  `id_diocesis` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `diocesis`
--

INSERT INTO `diocesis` (`id_diocesis`, `nombre`) VALUES
(1, 'Diócesis de Managua'),
(2, 'Diócesis de León'),
(3, 'Diócesis de Granada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `foto`
--

CREATE TABLE `foto` (
  `id_foto` int(11) NOT NULL,
  `foto` varchar(50) NOT NULL,
  `ubicacion` varchar(45) NOT NULL,
  `id_galeria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `galeria`
--

CREATE TABLE `galeria` (
  `id_galeria` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `portada` varchar(45) DEFAULT NULL,
  `id_templo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `galeria`
--

INSERT INTO `galeria` (`id_galeria`, `descripcion`, `portada`, `id_templo`) VALUES
(1, '', NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horario`
--

CREATE TABLE `horario` (
  `id_horario` int(11) NOT NULL,
  `hora` int(11) NOT NULL,
  `dia` int(11) NOT NULL,
  `id_servicio_religioso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `horario`
--

INSERT INTO `horario` (`id_horario`, `hora`, `dia`, `id_servicio_religioso`) VALUES
(1, 0, 0, 1),
(2, 0, 0, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipio`
--

CREATE TABLE `municipio` (
  `id_municipio` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `id_departamento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `municipio`
--

INSERT INTO `municipio` (`id_municipio`, `nombre`, `id_departamento`) VALUES
(1, NULL, 1),
(2, NULL, 2),
(3, NULL, 1),
(4, NULL, 1),
(5, NULL, 2),
(6, NULL, 2),
(7, NULL, 3),
(8, NULL, 3),
(9, NULL, 4),
(10, NULL, 4),
(11, NULL, 5),
(12, NULL, 5),
(13, NULL, 6),
(14, NULL, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia`
--

CREATE TABLE `noticia` (
  `id_noticia` int(11) NOT NULL,
  `titulo` varchar(45) DEFAULT NULL,
  `noticia` varchar(45) DEFAULT NULL,
  `imagen` varchar(45) DEFAULT NULL,
  `id_templo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `noticia`
--

INSERT INTO `noticia` (`id_noticia`, `titulo`, `noticia`, `imagen`, `id_templo`) VALUES
(1, NULL, NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `oficio_eclesiastico`
--

CREATE TABLE `oficio_eclesiastico` (
  `id_oficio_eclesiastico` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `oficio_eclesiastico`
--

INSERT INTO `oficio_eclesiastico` (`id_oficio_eclesiastico`, `tipo`) VALUES
(1, 'Párroco'),
(2, 'Vicario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presbitero`
--

CREATE TABLE `presbitero` (
  `id_presbitero` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `cane_confer` varchar(45) NOT NULL,
  `nombre_popular` varchar(45) NOT NULL,
  `fecha_ordenacion` int(11) NOT NULL,
  `foto_portada` varchar(45) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_templo` int(11) NOT NULL,
  `id_oficio_eclesiastico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `presbitero`
--

INSERT INTO `presbitero` (`id_presbitero`, `nombre`, `apellido`, `cane_confer`, `nombre_popular`, `fecha_ordenacion`, `foto_portada`, `id_usuario`, `id_templo`, `id_oficio_eclesiastico`) VALUES
(1, 'Leopoldo José', 'Brenes Solórzano', '7342', 'Polito', 123456789, 'img_user.jpg', 2, 1, 1),
(2, 'Julio Santos ', 'Dávila ', '1234', 'Nombre Popular', 987654321, 'presb.png', 3, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `privilegio`
--

CREATE TABLE `privilegio` (
  `id_privilegio` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `privilegio`
--

INSERT INTO `privilegio` (`id_privilegio`, `tipo`) VALUES
(1, 'crud'),
(2, 'ru');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio_religioso`
--

CREATE TABLE `servicio_religioso` (
  `id_servicio_religioso` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `templo_id_templo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `servicio_religioso`
--

INSERT INTO `servicio_religioso` (`id_servicio_religioso`, `tipo`, `descripcion`, `templo_id_templo`) VALUES
(1, 'Boda', '', 2),
(2, 'Bautizo', '', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `templo`
--

CREATE TABLE `templo` (
  `id_templo` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `nombre_popular` varchar(150) DEFAULT NULL,
  `direccion` varchar(500) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `historia` varchar(500) DEFAULT NULL,
  `nombre_institucion` varchar(100) NOT NULL,
  `portada` varchar(45) DEFAULT NULL,
  `georeferencia` varchar(45) DEFAULT NULL,
  `id_zona_parroquial` int(11) NOT NULL,
  `id_municipio` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `templo`
--

INSERT INTO `templo` (`id_templo`, `nombre`, `nombre_popular`, `direccion`, `telefono`, `historia`, `nombre_institucion`, `portada`, `institucion`, `id_zona_parroquial`, `id_municipio`, `id_categoria`) VALUES
(1, 'Catedral Metropolitana Inmaculada Concepción de María ', 'Catedral de Managua', 'Reparto Serrano, Costado sur DGI', '(505) 2278 4223 - 2278 4232 (oficina)', NULL, '', NULL, NULL, 1, 1, 1),
(2, 'Cristo Rey', NULL, 'Reparto Schick II Etapa, del Chaparral 1c. al norte', '(505) 2289 3911', NULL, '', NULL, NULL, 1, 1, 1),
(3, 'El Calvario', 'Iglesia del Oriental', 'Bo. Los Ángeles, Managua Costado sur donde fue la Shell. (Mercado Oriental)', '(505) 2248 1600', NULL, '', NULL, NULL, 1, 1, 1),
(4, 'Jesús de la Divina Misericordia ', NULL, 'Villa Fontana, Semáforo del Club Terraza \r\n2c. al oeste\r\n', '(505) 2270 6997', NULL, '', NULL, NULL, 1, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_actividad`
--

CREATE TABLE `tipo_actividad` (
  `id_tipo_actividad` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `id_actividad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `id_tipo_usuario` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `id_privilegio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`id_tipo_usuario`, `tipo`, `id_privilegio`) VALUES
(1, 'admin', 1),
(2, 'presbitero', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `email` varchar(45) NOT NULL,
  `contrasenha` varchar(200) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `is_active` tinyint(4) NOT NULL,
  `id_tipo_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `email`, `contrasenha`, `nombre`, `apellido`, `is_active`, `id_tipo_usuario`) VALUES
(1, 'admin@admin.com', 'pbkdf2:sha1:1000$CfJuntll$41578781605b8bca3dea44f84153646aa680246f', 'Admin', 'Nistrador', 1, 1),
(2, 'leopoldo@gmail.com', 'pbkdf2:sha1:1000$nfzAwZWX$c0299090704e840b0b8231788d89467ba9d5a0f8', 'Leopoldo', 'Brenes', 1, 2),
(3, 'sanjulio@mail.net', 'pbkdf2:sha1:1000$WewIMsXW$dafdca7488b483d6331bf9a63bdc4702491a2d51', 'Julio', 'Santos ', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zona_parroquial`
--

CREATE TABLE `zona_parroquial` (
  `id_zona_parroquial` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `id_zona_pastoral` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `zona_parroquial`
--

INSERT INTO `zona_parroquial` (`id_zona_parroquial`, `nombre`, `id_zona_pastoral`) VALUES
(1, 'Catedral Metropolitana Inmaculada Concepción de Maria', 1),
(2, 'Parroquia San Sebastian', 1),
(3, 'El Calvario', 1),
(4, 'Jesús de la Divina Misericordia', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zona_pastoral`
--

CREATE TABLE `zona_pastoral` (
  `id_zona_pastoral` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `id_diocesis` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `zona_pastoral`
--

INSERT INTO `zona_pastoral` (`id_zona_pastoral`, `nombre`, `id_diocesis`) VALUES
(1, 'Managua Central', 1),
(2, 'Managua Oriental', 1),
(3, 'Managua Occidental', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`id_actividad`),
  ADD KEY `id_templo` (`id_templo`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`);

--
-- Indices de la tabla `diocesis`
--
ALTER TABLE `diocesis`
  ADD PRIMARY KEY (`id_diocesis`);

--
-- Indices de la tabla `foto`
--
ALTER TABLE `foto`
  ADD PRIMARY KEY (`id_foto`),
  ADD KEY `id_galeria` (`id_galeria`);

--
-- Indices de la tabla `galeria`
--
ALTER TABLE `galeria`
  ADD PRIMARY KEY (`id_galeria`),
  ADD KEY `id_templo` (`id_templo`);

--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id_horario`),
  ADD KEY `id_servicio_religioso` (`id_servicio_religioso`);

--
-- Indices de la tabla `municipio`
--
ALTER TABLE `municipio`
  ADD PRIMARY KEY (`id_municipio`),
  ADD KEY `id_departamento` (`id_departamento`);

--
-- Indices de la tabla `noticia`
--
ALTER TABLE `noticia`
  ADD PRIMARY KEY (`id_noticia`),
  ADD KEY `id_templo` (`id_templo`);

--
-- Indices de la tabla `presbitero`
--
ALTER TABLE `presbitero`
  ADD PRIMARY KEY (`id_presbitero`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_templo` (`id_templo`),
  ADD KEY `id_oficio_eclesiastico` (`id_oficio_eclesiastico`);

--
-- Indices de la tabla `privilegio`
--
ALTER TABLE `privilegio`
  ADD PRIMARY KEY (`id_privilegio`);

--
-- Indices de la tabla `servicio_religioso`
--
ALTER TABLE `servicio_religioso`
  ADD PRIMARY KEY (`id_servicio_religioso`),
  ADD KEY `fk_oficio_religioso_templo1_idx` (`templo_id_templo`);

--
-- Indices de la tabla `templo`
--
ALTER TABLE `templo`
  ADD PRIMARY KEY (`id_templo`),
  ADD KEY `id_zona_parroquial` (`id_zona_parroquial`),
  ADD KEY `id_municipio` (`id_municipio`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `tipo_actividad`
--
ALTER TABLE `tipo_actividad`
  ADD PRIMARY KEY (`id_tipo_actividad`),
  ADD KEY `id_actividad` (`id_actividad`);

--
-- Indices de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`id_tipo_usuario`),
  ADD KEY `id_privilegio` (`id_privilegio`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_tipo_usuario` (`id_tipo_usuario`);

--
-- Indices de la tabla `zona_parroquial`
--
ALTER TABLE `zona_parroquial`
  ADD PRIMARY KEY (`id_zona_parroquial`),
  ADD KEY `id_zona_pastoral` (`id_zona_pastoral`);

--
-- Indices de la tabla `zona_pastoral`
--
ALTER TABLE `zona_pastoral`
  ADD PRIMARY KEY (`id_zona_pastoral`),
  ADD KEY `id_diocesis` (`id_diocesis`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividad`
--
ALTER TABLE `actividad`
  MODIFY `id_actividad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id_departamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT de la tabla `diocesis`
--
ALTER TABLE `diocesis`
  MODIFY `id_diocesis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `galeria`
--
ALTER TABLE `galeria`
  MODIFY `id_galeria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `horario`
--
ALTER TABLE `horario`
  MODIFY `id_horario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `municipio`
--
ALTER TABLE `municipio`
  MODIFY `id_municipio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT de la tabla `noticia`
--
ALTER TABLE `noticia`
  MODIFY `id_noticia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `presbitero`
--
ALTER TABLE `presbitero`
  MODIFY `id_presbitero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
