---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/add-adcentralaccesspolicymember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADCentralAccessPolicyMember
---

# 添加 ADCentralAccessPolicy 成员

## 摘要
将中央访问规则添加到 Active Directory 中的中央访问策略中。

## 语法

```
Add-ADCentralAccessPolicyMember [-WhatIf] [-Confirm] [-AuthType <ADAuthType>]
 [-Credential <PSCredential>] [-Identity] <ADCentralAccessPolicy>
 [-Members] <ADCentralAccessRule[]> [-PassThru] [-Server <String>] [<CommonParameters>]
```

## 描述

`Add-ADCentralAccessPolicyMember` cmdlet 用于将中央访问规则添加到 Active Directory 中的中央访问策略中。

## 示例

### 示例 1

```powershell
$params = @{
    Identity = 'Finance Policy'
    Member = 'Finance Documents Rule', 'Corporate Documents Rule'
}
Add-ADCentralAccessPolicyMember @params
```

此命令将中央访问规则“财务文件规则”（Finance Documents Rule）和“企业文件规则”（Corporate Documents Rule）添加到中央访问策略“财务策略”（Finance Policy）中。

### 示例 2

```powershell
Get-ADCentralAccessPolicy -Filter "Name -like 'Corporate*'" |
    Add-ADCentralAccessPolicyMember -Members 'Corporate Documents Rule'
```

这个命令会获取所有名称以“Corporate”开头的中央访问策略，然后通过管道运算符将这些信息传递给`Add-ADCentralAccessPolicyMember` cmdlet。`Add-ADCentralAccessPolicyMember` cmdlet随后会将名称为“Corporate Documents Rule”的中央访问规则添加到相应的配置中。

## 参数

### -AuthType

指定要使用的身份验证方法。该参数的可接受值为：

- `Negotiate` or `0`
- `Basic` or `1`

默认的身份验证方法是“Negotiate”。

对于“基本”（Basic）认证方法来说，需要使用安全套接字层（SSL）连接。

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

在运行该cmdlet之前，会提示您进行确认。

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

指定用于执行此任务的用户账户凭据。默认凭据是当前登录用户的凭据，除非该 cmdlet 是从 Windows PowerShell 提供程序的 Active Directory 模块驱动器中运行的。如果是从这样的驱动器中运行 cmdlet，则默认使用与该驱动器关联的账户的凭据。

要指定此参数，您可以输入一个用户名（例如 `User1` 或 `Domain01\User0`），或者可以指定一个 **PSCredential** 对象。如果您为该参数指定了一个用户名，cmdlet 会提示您输入密码。

你也可以通过编写脚本或使用 `Get-Credential` cmdlet 来创建一个 **PSCredential** 对象。之后，可以将这个 **PSCredential** 对象设置为相应的参数值。

如果执行任务的账户没有目录级别的权限，Windows PowerShell 的 Active Directory 模块会返回一个终止错误。

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

通过提供以下属性值之一来指定一个 Active Directory 对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (**objectGUID**)
- A security identifier (**objectSid**)
- A SAM account name (**sAMAccountName**)

This parameter can also get this object through the pipeline or you can set this parameter to an
object instance.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Members

Specifies a set of central access rule (CAR) objects in a comma-separated list to add to a central
access policy. To identify each object, use one of the following property values:

- Name
- A distinguished name
- GUID (**objectGUID**)

> [!NOTE]
> The identifier in parentheses is the LDAP display name.

You can also provide objects to this parameter directly.

You cannot pass objects through the pipeline to this parameter.

```yaml
Type: Microsoft.ActiveDirectory.Management.ADCentralAccessRule[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru

Returns an object representing the item with which you are working.
By default, this cmdlet does not generate any output.

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

### -Server

指定要连接的 Active Directory 域服务实例，为此需提供相应的域名或目录服务器的其中一个值。该服务可以是以下类型之一：Active Directory 轻量级域服务、Active Directory 域服务或 Active Directory 快照实例。

以下列方式之一指定 Active Directory 域服务实例：

域名值：

- Fully qualified domain name
- NetBIOS name

Directory server values:

- Fully qualified directory server name
- NetBIOS name
- Fully qualified directory server name and port

该参数的默认值是根据以下方法之一确定的，具体采用哪种方法取决于它们的排列顺序：

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

### 无或 Microsoft.ActiveDirectory.Management.ADCentralAccessPolicy

`Identity` 参数接收一个 `ADCentralAccessPolicy` 对象。

## 输出

### 无值或 Microsoft.ActiveDirectory.ADCentralAccessPolicy

当指定 `PassThru` 参数时，该 cmdlet 会返回修改后的 **ADCentralAccessPolicy** 对象。默认情况下，此 cmdlet 不生成任何输出。

## 备注

- This cmdlet does not work with a read-only domain controller.
- This cmdlet does not work with an Active Directory snapshot.

## 相关链接

[Remove-ADCentralAccessPolicyMember](./Remove-ADCentralAccessPolicyMember.md)

[Windows PowerShell中的AD DS管理Cmdlets](./activedirectory.md)
