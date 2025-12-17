---  
标题：关于 ActiveDirectory 身份验证  
日期：2013年4月22日  
描述：本文列出了 Windows PowerShell 中的 Active Directory 模块支持的用于搜索和检索的身份属性。  
区域设置：en-US  
模式：2.0.0

# 关于 Active Directory 身份管理

## 简短描述

Windows PowerShell中的Active Directory模块对象具有一系列用于搜索和检索的标识属性。

## 详细描述

为了识别 Active Directory 中的对象，每个对象都具有一些可以用作标识符的属性。在 Active Directory 模块中，可以通过 `Identity` 参数来传递对象的标识信息。每种对象类型都有自己的一组可供 `Identity` 参数使用的属性类型和值。有关其使用方法的更多详细信息，请参阅相应 cmdlet 的 `Identity` 参数的相关描述。

在使用 Active Directory 模块 cmdlets 进行搜索时，`Identity` 参数的值会与 `Server` 和 `Partition` 参数的值一起被用来唯一标识一个对象。`Server` 参数用于确定要连接到的服务器；`Partition` 参数则进一步将搜索范围缩小到特定的分区；最后，`Identity` 参数会将这个分区中的所有对象中唯一的一个识别出来。

请注意：当您使用安全账户管理器（Security Accounts Manager，简称SAM）中的账户名称（**sAMAccountName**）来访问全局目录端口时，如果您同时使用了“Identity”参数，那么在另一个域中将无法找到相应的用户。

如果通过身份解析找到多个对象，Active Directory 模块会抛出错误。

有关“Server”和“Partition”参数的更多信息，请参阅使用这些参数的各个cmdlet（例如`Get-ADUser`）的帮助主题。具体操作方法是：

```powershell
Get-Help Get-ADUser
```

### 对象与身份

每个对象都有一组属性，这些属性可以用来标识该对象。此外，如果某个对象是从另一个对象继承而来的，那么父对象的属性也可以作为子对象的标识符。有关 Active Directory 对象层次结构的更多信息，请参阅 [关于 ActiveDirectory 对象模型](about_ActiveDirectory_ObjectModel.md)。

> [注意] > 对于 Active Directory 提供程序的 cmdlet，只能使用对象的 “Distinguished Name” 或 “Relative Distinguished Name” 作为标识。有关 Active Directory 提供程序 cmdlet 的列表，请参阅 ActiveDirectory。

### 身份属性（Identity Attributes）

以下是按对象类型分类的身份属性列表。

- ADAccount
  - Distinguished Name
  - GUID (objectGUID)
  - Security Identifier (objectSid)
  - SAM Account Name (sAMAccountName)

- ADComputer
  - Distinguished Name
  - GUID  (objectGUID)
  - Security Identifier (objectSid)
  - Security Accounts Manager Account Name (sAMAccountName)

- ADDirectoryServer
  - Name of the server object (name)
    - For AD LDS instances the syntax of a name is `<computer-name>$<instance-name>`
    - For other Active Directory instances, use the value of the name property.
  - Distinguished Name of the NTDS Settings object
  - Distinguished Name of the server object that represents the directory
    server.
  - GUID (objectGUID) of server object under the configuration partition.
  - GUID (objectGUID) of NTDS settings object under the configuration partition

- ADDomain
  - Distinguished Name
  - GUID
  - Security Identifier
  - DNS domain name
  - NetBIOS domain name

- ADDomainController
  - GUID (objectGUID)
  - IPV4Address
  - Global IPV6Address
  - DNS Host Name (dNSHostName)
  - Name of the server object
  - Distinguished Name of the NTDS Settings object
  - Distinguished Name of the server object that represents the domain controller
  - GUID of NTDS settings object under the configuration partition
  - GUID of server object under the configuration partition
  - Distinguished Name of the computer object that represents the domain controller.

- ADFineGrainedPasswordPolicy
  - Distinguished Name
  - GUID (objectGUID)
  - Name (name)

- ADForest
  - Fully qualified domain name
  - DNS host name
  - NetBIOS name

- ADGroup
  - Distinguished Name
  - GUID (objectGUID)
  - Security Identifier (objectSid)
  - Security Accounts Manager (SAM) Account Name (sAMAccountName)

- ADObject
  - Distinguished Name
  - GUID (objectGUID)

- ADOptionalFeature
  - Distinguished Name
  - Name (name)
  - Feature GUID (featureGUID)
  - GUID (objectGUID)

- ADOrganizationalUnit
  - Distinguished Name
  - GUID (objectGUID)

- ADPrincipal
  - Distinguished Name
  - GUID (objectGUID)
  - Security Identifier (objectSid)
  - SAM Account Name (sAMAccountName)

- ADServiceAccount
  - Distinguished Name
  - GUID (objectGUID)
  - Security Identifier (objectSid)
  - SAM Account Name (sAMAccountName)

- ADUser
  - Distinguished Name
  - GUID (objectGUID)
  - Security Identifier (objectSid)
  - SAM User Name (sAMUserName)


### Identities Formats

Active Directory module objects have a range of identity attributes. Below is a
list of these, their types and formats.

- Distinguished Name
  - Example: CN=SaraDavis,CN=Europe,CN=Users, DC=corp,DC=contoso,DC=com

- DNS domain name
  - Example: redmond.corp.contoso.com

- DNS Host Name (dNSHostName)
  - Example: corp-DC01.corp.contoso.com

- Feature GUID (featureGUID)
  - Example: 599c3d2e-f72d-4d20-8a88-030d99495f20

- Fully qualified domain name
  - Example: corp.contoso.com

- Global IPV6Address
  - Example: 2001:4898:0:fff:200:5efe:157.59.132.61

- GUID (objectGUID)
  - Example: 599c3d2e-f72d-4d20-8a88-030d99495f20

- IPV4Address
  - Example:157.59.132.61

- NetBIOS domain name
  - Example: redmond

- Name of the server object
  - Example: corp-DC01$

- SAM Account Name (sAMAccountName)
  - Example: saradavisreports

- Security Identifier (objectSid)
  - Example: S-1-5-21-3165297888-301567370-576410423-1103

- Name
  - Example: Recycle Bin Feature
