---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/remove-adauthenticationpolicysilo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-ADAuthenticationPolicySilo
---

# 删除 ADAuthenticationPolicySilo

## 摘要
删除一个 Active Directory 域服务（AD DS）认证策略孤岛对象。

## 语法

```
Remove-ADAuthenticationPolicySilo [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Credential <PSCredential>]
 [-Identity] <ADAuthenticationPolicySilo> [-Server <String>] [<CommonParameters>]
```

## 描述
`Remove-ADAuthenticationPolicySilo` cmdlet 用于删除 Active Directory® 域服务中的身份验证策略隔离对象（即被单独管理的身份验证策略配置）。

`Identity` 参数用于指定要移除的 Active Directory 域服务（AD DS）身份验证策略孤岛。您可以通过该身份验证策略孤岛的 distinguished name、GUID 或名称来识别它。此外，您还可以使用 `Identity` 参数来指定一个包含该身份验证策略孤岛对象的变量，或者通过管道运算符将身份验证策略孤岛对象直接传递给 `Identity` 参数。

## 示例

### 示例 1：删除一个独立存在的身份验证策略对象
```
PS C:\> Remove-ADAuthenticationPolicySilo -Identity AuthenticationPolicySilo01
```

此命令会删除名为AuthenticationPolicySilo01的身份验证策略隔离对象（authentication policy silo object）。

### 示例 2：移除所有符合过滤条件的身份验证策略孤立对象
```
PS C:\> Get-ADAuthenticationPolicySilo -Filter 'Enforce -eq $False' | Remove-ADAuthenticationPolicySilo
```

此命令使用 `Get-ADAuthenticationPolicySilo` cmdlet 并结合 `Filter` 参数来获取所有未被强制执行的身份验证策略（即这些策略尚未被实际应用到系统中）。随后，管道操作符将过滤后的结果传递给 `Remove-ADAuthenticationPolicySilo` cmdlet，以便删除这些未强制执行的身份验证策略。

### 示例 3：在无需确认的情况下，移除所有匹配的身份验证策略孤立部分
```
PS C:\> Get-ADAuthenticationPolicySilo -Filter 'Enforce -eq $False' | Remove-ADAuthenticationPolicySilo -Confirm:$False
```

此命令使用了 **Get-ADAuthenticationPolicySilo** cmdlet 并配合 Filter 参数来获取所有未生效的认证策略（即那些未被实际应用的认证规则）。随后，管道运算符将过滤后的结果传递给 **Remove-ADAuthenticationPolicySilo** cmdlet。但由于 *Confirm* 参数被设置为 $False，因此不会显示任何确认提示信息。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值为：

- Negotiate or 0
- Basic or 1

默认的身份验证方法是“Negotiate”。对于基本身份验证方法（Basic authentication），需要建立安全套接字层（SSL）连接。

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

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个具有执行该任务权限的用户账户。默认值为当前用户。可以输入用户名（例如 User01 或 Domain01\User01），或者输入一个 **PSCredential** 对象（例如通过 **Get-Credential** cmdlet 生成的对象）。

默认情况下，该cmdlet会使用当前登录用户的凭据，除非它是从Active Directory域服务Windows PowerShell提供程序驱动器中运行的。如果该cmdlet是在提供程序驱动器中运行的，则默认使用的将是与该驱动器关联的账户。

如果你指定的凭据没有执行该任务的权限，那么此cmdlet会返回一个错误。

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
指定一个 Active Directory 域服务（Active Directory Domain Services）认证策略对象。请使用以下格式之一来指定该认证策略对象：

- A distinguished name
- GUID
- Name

This parameter can also get this object through the pipeline or you can set this parameter to an object instance.

The cmdlet searches the default naming context or partition to find the object.
If the cmdlet finds two or more objects, the cmdlet returns a non-terminating error.

```yaml
Type: ADAuthenticationPolicySilo
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Server
Specifies the Active Directory Domain Services instance to which to connect, by providing one of the following values for a corresponding domain name or directory server.
The service may be any of the following:  Active Directory Lightweight Domain Services, Active Directory Domain Services or Active Directory snapshot instance.

Specify the Active Directory Domain Services instance in one of the following ways:

Domain name values:

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

The default value for this parameter is determined by one of the following methods in the order that they are listed:

- By using the *Server* value from objects passed through the pipeline
- By using the server information associated with the Active Directory Domain Services Windows PowerShell provider drive, when the cmdlet runs in that drive
- By using the domain of the computer running Windows PowerShell

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management.ADAuthenticationPolicySilo
这个cmdlet接受一个身份验证策略对象（authentication policy object）。

## 输出

### System.Object

## 备注

## 相关链接

[Get-ADAuthenticationPolicySilo](./Get-ADAuthenticationPolicySilo.md)

[New-ADAuthenticationPolicySilo](./New-ADAuthenticationPolicySilo.md)

[Set-ADAuthenticationPolicySilo](./Set-ADAuthenticationPolicySilo.md)

[Windows PowerShell 中的 AD DS 管理 cmdlet](./activedirectory.md)

