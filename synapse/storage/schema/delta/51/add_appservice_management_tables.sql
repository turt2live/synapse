/* Copyright 2018 Travis Ralston
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */



CREATE TABLE IF NOT EXISTS application_services (
  id TEXT NOT NULL,
  as_token TEXT NOT NULL,
  hs_token TEXT NOT NULL,
  sender_localpart TEXT NOT NULL,
  url TEXT NULL,
  rate_limited BOOLEAN DEFAULT 0 NOT NULL,
  enabled BOOLEAN DEFAULT 0 NOT NULL,
  UNIQUE(id)
);

CREATE TABLE IF NOT EXISTS application_services_namespaces (
  id TEXT NOT NULL,
  namespace TEXT NOT NULL,
  regex TEXT NOT NULL,
  exclusive BOOLEAN DEFAULT 0 NOT NULL,
  group_id TEXT NOT NULL, -- only technically applies to user namespaces
);
