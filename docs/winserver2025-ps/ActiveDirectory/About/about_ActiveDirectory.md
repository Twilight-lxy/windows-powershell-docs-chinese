---  
标题：关于Active Directory  
日期：2013年4月22日  
描述：Active Directory模块是一个用于管理Active Directory的命令行接口。  
语言设置：en-US  
版本：2.0.0  
---

# 关于 Active Directory

## 简要描述

Active Directory 模块是一个用于管理 Active Directory 的命令行接口。

## 长描述

Windows PowerShell的Active Directory模块专为那些负责管理和使用Active Directory的系统管理员设计。该模块提供了一种高效的方式来执行各种管理、配置及诊断任务，这些任务涉及他们环境中的Active Directory域服务（AD DS）和Active Directory轻量级目录服务（AD LDS）实例。Active Directory模块包含一组Windows PowerShell cmdlet（命令行工具）以及一个用于访问Active Directory数据库的提供者（provider）。该提供者通过一种层次化的导航系统来展示Active Directory的数据结构，这种系统与文件系统的操作方式非常相似。就像文件系统中的驱动器（如C:）一样，你可以将Windows PowerShell的“驱动器”连接到Active Directory域或AD LDS服务器上，同时还可以访问Active Directory的快照数据。

### Active Directory 模块命令行的覆盖范围

对于 Active Directory 对象来说，`New-ADUser`、`Get-ADOrganizationalUnit`、`Set-ADComputer` 和 `Remove-ADUser` 等 cmdlet 支持创建（Create）、读取（Read）、更新（Update）和删除（Delete）操作。

账户和密码策略管理可以通过以下cmdlet来实现：`Enable-ADAccount`、`Unlock-ADAccount`、`New-ADServiceAccount`、`Set-ADAccountControl`以及`Remove-ADFineGrainedPasswordPolicy`。

域和林管理功能由以下命令let支持：`Get-ADForest`、`Set-ADForest`、`Set-ADForestMode`、`Enable-ADOptionalFeature`、`Get-ADDomainController` 以及 `Get-ADDomain`。

### 列出 Active Directory 模块命令行工具（Cmdlets）

要获取所有 Active Directory 模块 cmdlet 的列表，请运行

```powershell
Get-Command -Module ActiveDirectory
```

### 入门指南

开始使用 Windows PowerShell 的 Active Directory 模块非常简单，只需点击以下快捷方式即可：

在任意Windows PowerShell提示符中运行以下命令，以导入Active Directory模块：

```powershell
Import-Module ActiveDirectory
```

### 概述与概念性主题

其中前两个主题提供了关于Active Directory模块和Active Directory提供程序的高层次概述。

- For a brief introduction to the Active Directory provider for Windows
  PowerShell, see [ActiveDirectory](/powershell/module/activedirectory).
- The following topics are conceptual support topics for the Active Directory
  module cmdlets.
  - For an introduction to the **Identity** parameter, which is used by the
    Active Directory module cmdlets to identify objects in the directory, see
    [about_ActiveDirectory_Identity](about_ActiveDirectory_Identity.md).
  - For an introduction to the **Filter** parameter which is used by Active
    Directory module cmdlets to search for objects in the directory, see
    [about_ActiveDirectory_Filter](about_ActiveDirectory_Filter.md).
  - For an introduction to the .NET Framework-based object model implemented by
    the Active Directory module, see
    [about_ActiveDirectory_ObjectModel](about_ActiveDirectory_ObjectModel.md).
