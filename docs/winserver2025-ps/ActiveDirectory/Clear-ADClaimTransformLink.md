---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/clear-adclaimtransformlink?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-ADClaimTransformLink
---

# Clear-ADClaimTransformLink

## 摘要
删除对 Active Directory 中一个或多个跨林信任关系应用的声明转换（claims transformation）。

## 语法

```
Clear-ADClaimTransformLink [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADTrust> [-PassThru]
 [-Policy <ADClaimTransformPolicy>] [-Server <String>] [-TrustRole <ADTrustRole>]
 [<CommonParameters>]
```

## 描述

`Clear-ADClaimTransformLink` cmdlet 用于取消对 Active Directory 中一个或多个跨林信任关系应用的声明转换（claims transformation）。

## 示例

### 示例 1：从信任关系中删除指定的策略

```powershell
Clear-ADClaimTransformLink -Identity 'corp.contoso.com' -Policy DenyAllPolicy
```

此命令会从 `corp.contoso.com` 的信任关系中删除名为 `DenyAllPolicy` 的策略。

### 示例 2：移除所有应用于受信任森林（trusted forest）的政策

```powershell
Clear-ADClaimTransformLink -Identity 'corp.contoso.com' -TrustRole Trusted
```

此命令会删除所有应用于该林作为 `corp.contoso.com` 信任关系中受信任方的情况的策略。实际上，这个 cmdlet 会移除所有应用于从该林流向其信任伙伴的所有声明（claims）的策略。

### 示例 3：取消将某个理赔处理政策应用于信托关系

```powershell
$params = @{
    Identity = 'corp.contoso.com'
    Policy = 'DenyAllPolicy'
    TrustRole = 'Trusting'
}
Clear-ADClaimTransformLink @params
```

此命令会移除应用于该森林（在 `corp.contoso.com` 的信任关系中充当受信任域）的 `DenyAllPolicy` 策略。实际上，这个 cmdlet 会阻止 `DenyAllPolicy` 策略对来自其信任伙伴的所有身份验证请求（claims）生效。

## 参数

### -AuthType

指定要使用的认证方法。该参数的可接受值包括：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是`Negotiate`（协商）。

对于“基本”（Basic）身份验证方法来说，需要使用安全套接字层（SSL）连接。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果该 cmdlet 是从这样的驱动器中运行的，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User01`），或者可以指定一个 **PSCredential** 对象。如果您为此参数指定了一个用户名，该 cmdlet 会提示您输入密码。

你也可以通过脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，你可以将 **Credential** 参数设置为这个 **PSCredential** 对象。

如果该执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

通过提供以下值之一来指定一个 Active Directory 信任对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)

这个参数也可以通过管道获取该对象，或者你可以将该参数设置为一个对象实例。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADTrust
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不生成任何输出。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Policy

将指定的声明转换策略从应用于信任关系的配置中移除。

```yaml
Type: Microsoft.ActiveDirectory.Management.ADClaimTransformPolicy
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务（Active Directory Lightweight Domain Services）、Active Directory 域服务（Active Directory Domain Services）或 Active Directory 快照实例（Active Directory Snapshot Instance）。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

此参数的默认值是通过以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

- By using the **Server** value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows
  PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustRole

指定当前森林在由 **Identity** 参数指定的信任关系中的角色。该参数允许的值如下：

- `Trusted`: Specify this value if the current forest is the trusted forest.
- `Trusting`: Specify this value if the current forest is the trusting forest.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADTrustRole
Parameter Sets: (All)
Aliases:
Accepted values: Trusted, Trusting

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.ADTrust

`Identity` 参数接收了一个账户对象（类型为 `Microsoft.ActiveDirectory.Management.ADTrust`）。

## 输出

### 无

## 备注

## 相关链接

[Set-ADClaimTransformLink](./Set-ADClaimTransformLink.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
