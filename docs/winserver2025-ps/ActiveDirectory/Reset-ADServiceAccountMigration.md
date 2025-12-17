---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 02/15/2024
online version: https://learn.microsoft.com/powershell/module/activedirectory/reset-adserviceaccountMigration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-ADServiceAccountMigration
---

# 重置 ADServiceAccountMigration

## 摘要
将迁移的状态重置为委托给托管服务账户的状态，并解除该托管服务账户与用户账户之间的关联。

## 语法

### ADServiceAccountMigrationParameterSet（默认值）

```
Reset-ADServiceAccountMigration [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADServiceAccount> [-SupersededAccount <String>] [-Server <String>]
 [<CommonParameters>]
```

## 描述

`Reset-ADServiceAccountMigration` cmdlet 会重置迁移流程，将普通用户账户替换为由 **SupersededAccount** 参数指定的 distinguished name 字符串所代表的账户，并将该普通用户账户替换为由 **identity** 参数指定的委托管理服务账户。这两个账户之前必须已经通过 `Start-ADServiceAccountMigration` cmdlet 被关联起来。

**Identity** 参数用于指定要使用的委托管理服务账户。您可以通过该账户的独特名称、GUID、安全标识符（SID）或安全帐户管理器（SAM）账户名称来识别该管理服务账户。

`SupersededAccount` 参数指定了与被委托管理的服务账户关联的用户账户。该被替代账户必须通过其唯一标识名称（distinguished name）来识别。

## 示例

### 示例 1：使用委托管理的服务账户的安全账户管理器名称来重置该服务账户的迁移状态

```powershell
$params = @{
    Identity = "delegatedSvc1"
    SupersededAccount = "CN=User1,OU=Accounts,DC=Contoso,DC=com"
}
Reset-ADServiceAccountMigration @params
```

### 示例 2：通过指定一个 2025 年发布的域控制器来重置服务账户迁移过程

```powershell
$params = @{
    Identity = "delegatedSvc1"
    SupersededAccount = "CN=User1,OU=Accounts,DC=Contoso,DC=com"
    Server = "2025DC.Contoso.Com"
}
Reset-ADServiceAccountMigration @params
```

## 参数

### -AuthType

指定要使用的认证方法。此参数的可接受值包括：

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从此类驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 *Credential* 参数设置为这个 **PSCredential** 对象。

如果执行任务的账号没有目录级别的权限，Windows PowerShell的Active Directory模块会返回一个终止错误（即程序会立即退出）。

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

该cmdlet会在默认的命名上下文或分区中搜索目标对象。如果找到两个或多个对象，它会返回一个非终止性的错误（即无法继续执行的错误）。

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

指定您希望迁移到委托托管服务账户的用户账户。该账户必须通过其唯一名称（Distinguished Name）来标识。

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

指定要连接的 Active Directory 域服务实例，为此需提供一个对应的域名或目录服务器的名称。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot instance）。

域名值：

- Fully qualified domain name (FQDN)
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

**Server** 参数的默认值是通过以下方法之一确定的，具体使用哪种方法取决于它们在列表中的排列顺序：

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

此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft ActiveDirectory.Management.ADServiceAccount

由 **Identity** 参数接收一个委托管理的托管服务账户对象（delegated managed service account object）。

## 备注

- This cmdlet doesn't work with AD LDS.
- This cmdlet doesn't work with an Active Directory snapshot.
- This cmdlet doesn't work with a read-only domain controller.
- This cmdlet requires that you create a Microsoft Group Key Distribution Service (GKDS) root key
  first to begin using group managed service accounts in your Active Directory deployment. For more
  information on how to create the GKDS root key using Windows PowerShell, see
  [Create the Key Distribution Services KDS Root Key](https://go.microsoft.com/fwlink/?LinkId=253584).

## 相关链接

[完成广告服务账户迁移](./Complete-AdServiceAccountMigration.md)

[开始 AdService 账户迁移](./Start-AdServiceAccountMigration.md)

[撤销 AdService 账户迁移操作](./Undo-AdServiceAccountMigration.md)

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)
