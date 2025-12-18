---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.BestPractices.Cmdlets.dll-Help.xml
Module Name: BestPractices
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/bestpractices/invoke-bpamodel?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Invoke-BpaModel
---

#Invoke-BpaModel

## 摘要
开始对计算机上安装的特定模型进行BPA（业务过程分析）扫描。

## 语法

### ModelParameterSet（默认值）
```
Invoke-BpaModel [-ModelId] <String> [-RepositoryPath <String>] [-Mode <ScanMode>] [<CommonParameters>]
```

### SubModelParameterSet
```
Invoke-BpaModel [-ModelId] <String> [-RepositoryPath <String>] [-Mode <ScanMode>] [-SubModelId <String>]
 [-Context <String>] [-ComputerName <String[]>] [-CertificateThumbprint <String>] [-ConfigurationName <String>]
 [-Credential <PSCredential>] [-Authentication <AuthenticationMechanism>] [-Port <Int32>]
 [-ThrottleLimit <Int32>] [-UseSsl] [<CommonParameters>]
```

## 描述
`Invoke-BpaModel` cmdlet 用于对安装在基于 Windows 的计算机上的特定模型启动 Best Practices Analyzer (BPA) 扫描。该模型的指定可以通过使用 `ModelId` 参数来完成，或者将 `Get-BpaModel` cmdlet 的输出结果通过管道传递给该 cmdlet 来实现。如果在 BPA 扫描完成后才在 cmdlet 中指定模型，则扫描结果将以 XML 文件的形式提供。

此 cmdlet 一旦启动后就无法取消。

BPA模型架构不支持单节点XML格式的数据。

## 示例

### 示例 1：为指定的模型 ID 启动 BPA 扫描
```
PS C:\> Invoke-BPAModel -ModelId "ModelId1"
```

这个示例会对由 ModelId1 表示的模型启动 BPA（Business Process Analysis，业务流程分析）扫描。

可以通过运行以下任意一个 cmdlet 来完成相同的任务。


`Invoke-BPAModel -Id "ModelId1"`

或者

`Invoke-BPAModel "ModelId1"`

### 示例 2：使用管道启动 BPA 扫描
```
PS C:\> Get-BPAModel | Invoke-BPAModel
```

这个示例会获取计算机上安装的所有BPA模型，然后将`Get-BpaModel` cmdlet的输出结果传递给另一个cmdlet，以便对所有模型执行BPA扫描。

### 示例 3：启动 BPA 扫描并将结果保存到一个变量中
```
PS C:\> $BPAObj = Invoke-BPAModel ModelId1


This cmdlet displays the results of any specific object in the previous cmdlet by calling the variable into which the results of the previous cmdlet were saved, and then specifying the object in the results that the administrator wants. The object is identified by its numerical order in the collection of results (the [CODE_Snippit]0[CODE_Snippit], or first, object). The cmdlet then identifies which field of the results in that object (for this example, the Detail field) the administrator wants to view. The cmdlet shown returns the properties of the Detail field from the first object in the results of the preceding line.
PS C:\> $BPAObj[0].Detail
ModelId             : ModelId1
Success             : True
ScanTime            : 10/21/2008 3:08:47 PM
InformationMessages : 5
WarningMessages     : 4
ErrorMessages       : 0
Description         :
```

这个示例在由 ModelId1 指定的模型上启动了一个 BPA 扫描，并将该cmdlet的结果保存到一个变量 $BPAObj 中。

## 参数

### -Authentication
指定在创建用于执行远程BPA扫描的远程连接时使用的身份验证模式。有关更多信息，请输入`Get-HelpInvoke-Command`。

```yaml
Type: AuthenticationMechanism
Parameter Sets: SubModelParameterSet
Aliases:
Accepted values: Default, Basic, Negotiate, NegotiateWithImplicitCredential, Credssp, Digest, Kerberos

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CertificateThumbprint
指定在通过 SSL 创建远程连接以执行远程 BPA 扫描时使用的证书指纹。有关更多信息，请键入 `Get-Help Invoke-Command`。

```yaml
Type: String
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定用于运行BPA扫描的目标计算机。

```yaml
Type: String[]
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ConfigurationName
用于指定会话配置（例如端点的名称），以便在为远程BPA扫描创建会话时使用这些配置。有关更多信息，请输入 `Get-Help Invoke-Command`。

```yaml
Type: String
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Context
在特定模型的背景下扫描某个子模型（该子模型与父模型不同）。例如，管理员希望对SQL模型的“Backend”子模型进行扫描，但仅限于在第三个模型的上下文中进行扫描；这个第三方模型依赖于SQL Server技术。

```yaml
Type: String
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定在创建远程连接以执行远程BPA扫描时使用的凭据。有关更多信息，请输入 `Get-HelpInvoke-Command`。

```yaml
Type: PSCredential
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Mode
指定在运行BPA扫描时使用的模式。该参数的可接受值为：All（全部）、Analysis（分析）或Discovery（发现）。

```yaml
Type: ScanMode
Parameter Sets: (All)
Aliases:
Accepted values: All, Discovery, Analysis

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ModelId
确定将用于BPA扫描的模型。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Id, BestPracticesModelId

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Port
指定在创建远程连接以执行远程BPA扫描时使用的端口。有关更多信息，请输入`Get-Help Invoke-Command`。

```yaml
Type: Int32
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RepositoryPath
指定应覆盖由 `ReportsRoot` 注册表键指定的报告的默认存储位置。该参数指定了结果应存储的路径。

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

### -SubModelId
用于确定要为由*ModelId*参数指定的模型运行的子模型。例如，Update Services模型（`Microsoft/Windows/UpdateServices`）有两个子模型（`UpdateServices-DB`、`UpdateServices-Services`）。

```yaml
Type: String
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定在创建用于执行远程BPA扫描的远程连接时使用的节流限制。有关更多信息，请输入 `Get-Help Invoke-Command`。

```yaml
Type: Int32
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseSsl
指定在创建用于执行远程BPA扫描的远程连接时是否使用SSL。有关更多信息，请输入`Get-Help Invoke-Command`。

```yaml
Type: SwitchParameter
Parameter Sets: SubModelParameterSet
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String
由 *ModelId* 参数指定的输入字符串。

## 输出

### System.Collections.Generic.List<Microsoft.BestPractices.CoreInterface.InvokeBpaModelOutput>
输出对象封装了所输入的cmdlet的执行结果。该输出对象包含了诸如BPA模型ID、cmdlet的执行是否成功以及其他详细信息等内容。

## 备注

## 相关链接

[Get-BpaModel](./Get-BpaModel.md)

[Get-BpaResult](./Get-BpaResult.md)

[Set-BpaResult](./Set-BpaResult.md)

