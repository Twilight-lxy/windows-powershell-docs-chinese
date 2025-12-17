---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/get-adrootdse?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ADRootDSE
---

# Get-ADRootDSE

## 摘要
获取目录服务器信息树的根节点。

## 语法

```
Get-ADRootDSE [-AuthType <ADAuthType>] [-Credential <PSCredential>] [-Properties <String[]>] [-Server <String>]
 [<CommonParameters>]
```

## 描述
**Get-ADRootDSE** cmdlet 用于获取表示目录服务器的目录信息树根部的对象。该目录信息树提供了有关目录服务器配置和功能的信息，例如配置容器的 distinguished name（唯一名称）、目录服务器上的当前时间以及目录服务器和域的功能级别等。

## 示例

### 示例 1：获取目录服务器信息树的根节点
```
PS C:\> Get-ADRootDSE
configurationNamingContext    : CN=Configuration,DC=Fabrikam,DC=com
currentTime                   : 3/18/2009 11:12:55 AM
defaultNamingContext          : DC=Fabrikam,DC=com
dnsHostName                   : FABRIKAM-DC1.Fabrikam.com
domainControllerFunctionality : Windows2008R2
domainFunctionality           : Windows2003Domain
dsServiceName                 : CN=NTDS Settings,CN=FABRIKAM-DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=Fabrikam,DC=com
forestFunctionality           : Windows2003Forest
highestCommittedUSN           : 23015
isGlobalCatalogReady          : {TRUE}
isSynchronized                : {TRUE}
ldapServiceName               : Fabrikam.com:FABRIKAM-DC1$@FABRIKAM.COM
namingContexts                : {DC=Fabrikam,DC=com, CN=Configuration,DC=Fabrikam,DC=com, CN=Schema,CN=Configuration,DC=Fabrikam,DC=com, DC=DomainDnsZones,DC=Fabrikam,DC=com...}
rootDomainNamingContext       : DC=Fabrikam,DC=com
schemaNamingContext           : CN=Schema,CN=Configuration,DC=Fabrikam,DC=com
serverName                    : CN=FABRIKAM-DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=Fabrikam,DC=com
subschemaSubentry             : CN=Aggregate,CN=Schema,CN=Configuration,DC=Fabrikam,DC=com
supportedCapabilities         : {1.2.840.113556.1.4.800 (LDAP_CAP_ACTIVE_DIRECTORY_OID), 1.2.840.113556.1.4.1670 (LDAP_CAP_ACTIVE_DIRECTORY_V51_OID), 1.2.840.113556.1.4.1791 (LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID), 1.2.840.113556.1.4.1935 (LDAP_CAP_ACTIVE_DIRECTORY_V61_OID)...}
supportedControl              : {1.2.840.113556.1.4.319 (LDAP_PAGED_RESULT_OID_STRING), 1.2.840.113556.1.4.801 (LDAP_SERVER_SD_FLAGS_OID), 1.2.840.113556.1.4.473 (LDAP_SERVER_SORT_OID), 1.2.840.113556.1.4.528 (LDAP_SERVER_NOTIFICATION_OID)...}
supportedLDAPPolicies         : {MaxPoolThreads, MaxDatagramRecv, MaxReceiveBuffer, InitRecvTimeout...}
supportedLDAPVersion          : {3, 2}
supportedSASLMechanisms       : {GSSAPI, GSS-SPNEGO, EXTERNAL, DIGEST-MD5}
```

这个命令从默认的域控制器中获取目录服务器的信息树的根节点。

### 示例 2：获取具有指定属性的目录服务器信息树的根节点
```
PS C:\> Get-ADRootDSE -Server Fabrikam-RODC1 -Properties supportedExtension
configurationNamingContext    : CN=Configuration,DC=Fabrikam,DC=com
currentTime                   : 3/18/2009 11:12:55 AM
defaultNamingContext          : DC=Fabrikam,DC=com
dnsHostName                   : FABRIKAM-RODC1.Fabrikam.com
domainControllerFunctionality : Windows2008R2
domainFunctionality           : Windows2003Domain
dsServiceName                 : CN=NTDS Settings,CN=FABRIKAM-RODC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=Fabrikam,DC=com
forestFunctionality           : Windows2003Forest
highestCommittedUSN           : 23015
isGlobalCatalogReady          : {TRUE}
isSynchronized                : {TRUE}
ldapServiceName               : Fabrikam.com:FABRIKAM-RODC1$@FABRIKAM.COM
namingContexts                : {DC=Fabrikam,DC=com, CN=Configuration,DC=Fabrikam,DC=com, CN=Schema,CN=Configuration,DC=Fabrikam,DC=com, DC=DomainDnsZones,DC=Fabrikam,DC=com...}
rootDomainNamingContext       : DC=Fabrikam,DC=com
schemaNamingContext           : CN=Schema,CN=Configuration,DC=Fabrikam,DC=com
serverName                    : CN=FABRIKAM-RODC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=Fabrikam,DC=com
subschemaSubentry             : CN=Aggregate,CN=Schema,CN=Configuration,DC=Fabrikam,DC=com
supportedCapabilities         : {1.2.840.113556.1.4.800 (LDAP_CAP_ACTIVE_DIRECTORY_OID), 1.2.840.113556.1.4.1670 (LDAP_CAP_ACTIVE_DIRECTORY_V51_OID), 1.2.840.113556.1.4.1791 (LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID), 1.2.840.113556.1.4.1935 (LDAP_CAP_ACTIVE_DIRECTORY_V61_OID)...}
supportedControl              : {1.2.840.113556.1.4.319 (LDAP_PAGED_RESULT_OID_STRING), 1.2.840.113556.1.4.801 (LDAP_SERVER_SD_FLAGS_OID), 1.2.840.113556.1.4.473 (LDAP_SERVER_SORT_OID), 1.2.840.113556.1.4.528 (LDAP_SERVER_NOTIFICATION_OID)...}
supportedExtension            : {1.3.6.1.4.1.1466.20037, 1.3.6.1.4.1.1466.101.119.1, 1.2.840.113556.1.4.1781, 1.3.6.1.4.1.4203.1.11.3}
supportedLDAPPolicies         : {MaxPoolThreads, MaxDatagramRecv, MaxReceiveBuffer, InitRecvTimeout...}
supportedLDAPVersion          : {3, 2}
supportedSASLMechanisms       : {GSSAPI, GSS-SPNEGO, EXTERNAL, DIGEST-MD5}
```

该命令用于获取目录服务器信息树的根节点内容，其中包括Fabrikam-RODC1服务器的**supportedExtension**属性。

### 示例 3：使用凭据获取目录服务器信息树的根节点
```
PS C:\> Get-ADRootDSE -Server "FABRIKAM-ADLDS1.Fabrikam.com:60000" -Credential "FABRIKAM\User1"
configurationNamingContext    : CN=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}
currentTime                   : 3/18/2009 11:40:19 AM
dnsHostName                   : FABRIKAM-ADLDS1.Fabrikam.com
domainControllerFunctionality : Windows2008R2
dsServiceName                 : CN=NTDS Settings,CN=FABRIKAM-ADLDS1$instance1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,C
N=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}
forestFunctionality           : Windows2003Forest
highestCommittedUSN           : 13967
isSynchronized                : {TRUE}
namingContexts                : {CN=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}, CN=Schema,CN=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}, DC=AppNC}
schemaNamingContext           : CN=Schema,CN=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}
serverName                    : CN=FABRIKAM-ADLDS1$instance1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}
subschemaSubentry             : CN=Aggregate,CN=Schema,CN=Configuration,CN={9131D98B-E210-480F-A95D-24F9396898CA}
supportedCapabilities         : {1.2.840.113556.1.4.1851 (LDAP_CAP_ACTIVE_DIRECTORY_ADAM_OID), 1.2.840.113556.1.4.1670 (LDAP_CAP_ACTIVE_DIRECTORY_V51_OID), 1.2.840.113556.1.4.1791 (LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID), 1.2.840.113556.1.4.1935 (LDAP_CAP_ACTIVE_DIRECTORY_V61_OID)...}
supportedControl              : {1.2.840.113556.1.4.319 (LDAP_PAGED_RESULT_OID_STRING), 1.2.840.113556.1.4.801 (LDAP_SERVER_SD_FLAGS_OID), 1.2.840.113556.1.4.473 (LDAP_SERVER_SORT_OID), 1.2.840.113556.1.4.528 (LDAP_SERVER_NOTIFICATION_OID)...}
supportedLDAPPolicies         : {MaxPoolThreads, MaxDatagramRecv, MaxReceiveBuffer, InitRecvTimeout...}
supportedLDAPVersion          : {3, 2}
supportedSASLMechanisms       : {GSSAPI, GSS-SPNEGO, EXTERNAL, DIGEST-MD5}
```

该命令使用 FABRIKAM\user1 的凭据来获取 FABRIKAM-ADLDS1 目录服务器信息树的根目录。

## 参数

### -AuthType
指定要使用的身份验证方法。此参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认凭据将是与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 User1 或 Domain01\User01），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 `PSCredential` 对象。之后，你可以将 `Credential` 参数设置为这个 `PSCredential` 对象。

如果执行该任务的权限不足（即没有目录级别的权限），Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Properties
用于指定从服务器检索的输出对象的属性。使用此参数可以获取默认集合中未包含的属性。

为该参数指定属性，可以使用逗号分隔的名称列表。若要显示对象上设置的所有属性，请使用 *（星号）。

要指定某个特定的扩展属性，请使用该属性的名称。对于非默认属性或扩展属性，您必须指定该属性在LDAP中的显示名称。

要检索对象的属性并将其显示出来，你可以使用与该对象关联的 `Get-*` cmdlet，并将输出结果传递给 `Get-Member` cmdlet。有关更多信息，请输入 `Get-Help Get-Member`。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: Property

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定要连接的 Active Directory 域服务实例，为此需要提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

*Server* 参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using *Server* value from objects passed through the pipeline.
- By using the server information associated with the Active Directory PowerShell provider drive, when running under that drive.
- By using the domain of the computer running PowerShell.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ActiveDirectory.Management.ADRootDSE
此cmdlet会输出一个`ADRootDSE`对象，该对象代表了指定目录服务器的数据结构（即数据树）。

## 备注

## 相关链接

