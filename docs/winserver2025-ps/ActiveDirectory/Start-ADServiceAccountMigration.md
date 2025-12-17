---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 02/15/2024
online version: https://learn.microsoft.com/powershell/module/activedirectory/start-adserviceaccountMigration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-ADServiceAccountMigration
---

# 启动 AD 服务账户迁移

## 摘要
通过将一个普通用户账户与一个委托管理的服务账户关联起来，启动迁移过程。

## 语法

### ADServiceAccountMigrationParameterSet（默认值）

```
Start-ADServiceAccountMigration [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADServiceAccount> [-SupersededAccount <String>] [-Server <String>]
 [<CommonParameters>]
```

## 描述

`Start-ADServiceAccountMigration` cmdlet 将开始迁移过程，该过程会将由 **SupersededAccount** 参数提供的普通用户账户替换为由 **Identity** 参数提供的委托管理服务账户。

`Identity` 参数指定了要使用的委托托管服务账户。您可以通过该托管服务账户的独特名称、GUID、安全标识符（SID）或安全帐户管理器（SAM）账户名称来识别它。

`SupersededAccount` 参数指定了您希望关联到委托管理的服务账户的用户账户。被替代的账户必须通过其唯一名称来识别。

## 示例

#### 示例 1：使用委托管理的托管服务账户的安全帐户管理器名称来启动服务账户迁移过程

```powershell
$params = @{
    Identity = "delegatedSvc1"
    SupersededAccount = "CN=User1,OU=Accounts,DC=Contoso,DC=com"
}
Start-ADServiceAccountMigration @params
```

### 示例 2：通过指定一个 2025 年使用的域控制器来启动服务账户迁移过程

```powershell
$params = @{
    Identity = "delegatedSvc1"
    SupersededAccount = "CN=User1,OU=Accounts,DC=Contoso,DC=com"
    Server = "2025DC.Contoso.com"
}
Start-ADServiceAccountMigration @params
```

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

### -Identity

通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，它会返回一个无法终止的错误（即程序会无限循环执行，而不会停止）。

```yaml
Type: ADServiceAccount
Parameter Sets: ADServiceAccountMigrationParameterSet
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SupersededAccount

指定您希望迁移到委托管理服务账户的用户帐户。该帐户必须通过其唯一名称（Distinguished Name）来标识。

```yaml
Type: String
Parameter Sets: ADServiceAccountMigrationParameterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的值之一。该服务可以是以下类型中的任意一种：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

**Server** 参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们在列表中的顺序：

- By using **Server** value from objects passed through the pipeline.
- By using the server information associated with the Active Directory PowerShell provider drive,
  when running under that drive.
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

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.ADServiceAccount

一个委托管理的托管服务账户对象是通过 **Identity** 参数接收到的。

## 备注

- This cmdlet doesn't work with AD LDS.
- This cmdlet doesn't work with an Active Directory snapshot.
- This cmdlet doesn't work with a read-only domain controller.
- This cmdlet requires that you create a Microsoft Group Key Distribution Service (GKDS) root key
  first to begin using group managed service accounts in your Active Directory deployment. For more
  information on how to create the GKDS root key using Windows PowerShell, see
  [Create the Key Distribution Services KDS Root Key](https://go.microsoft.com/fwlink/?LinkId=253584).

## 相关链接

[完成 AD 服务账户迁移](./Complete-ADServiceAccountMigration.md)

[Reset-ADServiceAccountMigration](./Reset-ADServiceAccountMigration.md)

[撤销 ADServiceAccount 迁移操作](./Undo-ADServiceAccountMigration.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)
