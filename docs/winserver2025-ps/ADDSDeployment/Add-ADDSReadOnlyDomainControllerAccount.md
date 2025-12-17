---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.DirectoryServices.Deployment.dll-Help.xml
Module Name: ADDSDeployment
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/addsdeployment/add-addsreadonlydomaincontrolleraccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ADDSReadOnlyDomainControllerAccount
---

# 添加 AD DS 仅读域控制器账户

## 摘要
创建一个 RODC（域控制器操作主节点）账户，该账户可用于在 Active Directory 中安装 RODC。

## 语法

```
Add-ADDSReadOnlyDomainControllerAccount [-SkipPreChecks]
 -DomainControllerAccountName <String> -DomainName <String>
 -SiteName <String> [-AllowPasswordReplicationAccountName <String[]>]
 [-Credential <PSCredential>] [-DelegatedAdministratorAccountName <String>]
 [-DenyPasswordReplicationAccountName <String[]>] [-NoGlobalCatalog] [-InstallDns]
 [-ReplicationSourceDC <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Add-ADDSReadOnlyDomainControllerAccount` cmdlet 用于创建一个只读域控制器（RODC）账户，该账户可用于在 Active Directory 中安装 RODC。

## 示例

### 示例 1：添加一个 RODC 账户

```powershell
$HashArguments = @{
    DomainControllerAccountName = "RODC1"
    DomainName                  = "corp.contoso.com"
    SiteName                    = "NorthAmerica"
}
Add-ADDSReadOnlyDomainControllerAccount @HashArguments
```

此命令使用北美站点作为复制源域控制器的源站点，将一个RODC账户添加到`corp.contoso.com`域名中。

## 参数

### -AllowPasswordReplicationAccountName

指定一个用户账户、组账户和计算机账户的数组，这些账户的密码可以复制到这个RODC（Replicated Operations Domain Controller）中。如果希望该数组为空，请使用“None”。默认情况下，只有“Allowed RODC Password Replication Group”（允许的RODC密码复制组）是可用的，而该组最初是创建时为空的。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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

指定用于安装域控制器的账户的用户名和密码。在使用此参数时，请使用 `Get-Credential` cmdlet 来提示用户输入密码。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DelegatedAdministratorAccountName

指定安装和管理 RODC 的用户或组的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DenyPasswordReplicationAccountName

指定那些用户账户、组账户和计算机账户的名称，这些账户的密码将不会被复制到这个 RODC（Replicated Operations Domain Controller）中。如果您不希望拒绝任何用户或计算机的凭据复制，请使用“None”。默认情况下，管理员（Administrators）、服务器操作员（Server Operators）、备份操作员（Backup Operators）、账户操作员（Account Operators）以及“Denied RODC Password Replication Group”组会被禁止访问该功能。这个“Denied RODC Password Replication Group”组包括证书发布者（Cert Publishers）、域管理员（Domain Admins）、企业级管理员（Enterprise Admins）、企业级只读域控制器（Enterprise Read-Only Domain Controllers）、组策略创建者所有者（Group Policy Creator Owners）、krbtgt 账户以及架构管理员（Schema Admins）。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainControllerAccountName

指定此cmdlet创建的RODC账户的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainName

指定用于操作的用户名的域名。此参数是必需的。它还有助于确定您计划安装域控制器或创建RODC账户的森林（domain tree）。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

强制命令运行，而无需请求用户确认。

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

### -InstallDns

表示该 cmdlet 用于安装 DNS 服务器服务。如果未提供任何值，默认行为将根据现有环境自动计算 DNS 配置设置。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoGlobalCatalog

这表示该 cmdlet 不会将 RODC 设置为全局目录服务器。

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

### -ReplicationSourceDC

指定要用作复制到此RODC的源的域控制器的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: NULL
Accept pipeline input: False
Accept wildcard characters: False
```

### -SiteName

指定一个现有站点的名称，在该站点上可以放置新的域控制器。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: <mandatory>
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipPreChecks

该参数表示 cmdlet 仅执行一组基本的验证操作。这种行为相当于在早期版本的 Windows Server 中使用 `Dcpromo.exe` 添加域控制器时所执行的验证过程。当设置此开关参数时，它表示应跳过一些额外的初步检查。有关 **ADDSDeployment** 模块在使用 Windows Server 2012 时默认执行的这些额外初步检查的详细信息，请参阅 [AD DS 简化管理](https://go.microsoft.com/fwlink/?LinkID=237244) 中“ADPrep 和先决条件检查架构”部分中的表格。

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

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

- Once you have added the RODC account, you can add an RODC to a server computer by using the
  `Install-ADDSDomainController` cmdlet with the `-ReadOnlyReplica` switch parameter.
- You can also delegate the ability to attach the server to a non-administrative group or user. If
  you are deploying RODCs in delegated administration scenarios where the machine accounts are
  pre-provisioned, creating the RODC account is the first stage of the RODC installation process and
  needs to be done by a member of the Domain Admins group. In these scenarios, once an administrator
  uses this cmdlet to add the RODC account in Active Directory Domain Services (AD DS), the second
  stage of the installation can occur. This involves attaching an actual server computer in a remote
  location (such as a branch office) that will operate as the RODC for the specified account created
  using this cmdlet.

## 相关链接

[简化 AD DS 管理](https://go.microsoft.com/fwlink/?LinkID=237244)

[安装 ADDSDomainController](./Install-ADDSDomainController.md)

[获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)
